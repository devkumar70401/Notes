#!/usr/bin/env python3
"""
=============================================================================
👑 Unsloth Qwen 3.8 (27B) GGUF Lifecycle & Resilient Downloader
-----------------------------------------------------------------------------
Module: /home/dev/SE/Library/Models/qwen3.8.py
Repository: unsloth/Qwen3.8-27B-GGUF
Description: Production-grade utility to safely download, verify, and inspect
             official Unsloth Qwen 3.8 27B GGUF quantized models with pre-flight
             disk validation, auto-resumable chunked transfers, and hardware auditing.
=============================================================================
"""

import os
import sys
import shutil
import argparse
import signal
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any

try:
    import psutil
except ImportError:
    psutil = None

try:
    from huggingface_hub import hf_hub_download
except ImportError:
    hf_hub_download = None


# =============================================================================
# 🧭 Unsloth Qwen 3.8 GGUF Quantization Presets Matrix
# =============================================================================

@dataclass(frozen=True)
class ModelPreset:
    key: str
    name: str
    repo_id: str
    filename: str
    estimated_size_gb: float
    quant_type: str
    min_ram_vram_gb: float
    recommended_for: str
    description: str


PRESETS: Dict[str, ModelPreset] = {
    "q4_k_m": ModelPreset(
        key="q4_k_m",
        name="Qwen 3.8 27B (Q4_K_M) - ⭐ RECOMMENDED",
        repo_id="unsloth/Qwen3.8-27B-GGUF",
        filename="Qwen3.8-27B-Q4_K_M.gguf",
        estimated_size_gb=17.1,
        quant_type="4-bit Medium K-Quant",
        min_ram_vram_gb=24.0,
        recommended_for="Best overall balance of speed, intelligence, and memory.",
        description="The gold-standard 4-bit quantization with near-zero perplexity loss for coding, agentic reasoning, and chat."
    ),
    "q5_k_m": ModelPreset(
        key="q5_k_m",
        name="Qwen 3.8 27B (Q5_K_M) - High Precision",
        repo_id="unsloth/Qwen3.8-27B-GGUF",
        filename="Qwen3.8-27B-Q5_K_M.gguf",
        estimated_size_gb=19.8,
        quant_type="5-bit Medium K-Quant",
        min_ram_vram_gb=28.0,
        recommended_for="Maximum accuracy for complex mathematics, coding, and logical reasoning.",
        description="5.5-bit high-fidelity weights preserving subtle nuances and complex multi-step reasoning chains."
    ),
    "ud_q4_k_xl": ModelPreset(
        key="ud_q4_k_xl",
        name="Qwen 3.8 27B (UD-Q4_K_XL) - Unsloth Dynamic V3",
        repo_id="unsloth/Qwen3.8-27B-GGUF",
        filename="Qwen3.8-27B-UD-Q4_K_XL.gguf",
        estimated_size_gb=17.9,
        quant_type="Unsloth Dynamic 4-bit XL",
        min_ram_vram_gb=26.0,
        recommended_for="Enhanced attention layer fidelity via Unsloth Dynamic V3 quantization.",
        description="Custom Unsloth dynamic matrix scaling optimized for developer role tools and MTP."
    ),
    "q3_k_m": ModelPreset(
        key="q3_k_m",
        name="Qwen 3.8 27B (Q3_K_M) - Lightweight",
        repo_id="unsloth/Qwen3.8-27B-GGUF",
        filename="Qwen3.8-27B-Q3_K_M.gguf",
        estimated_size_gb=13.8,
        quant_type="3-bit Medium K-Quant",
        min_ram_vram_gb=16.0,
        recommended_for="Consumer workstations and laptops with 16 GB RAM.",
        description="Compact 3-bit quantization allowing the 27B model to run comfortably on 16GB system memory."
    ),
    "q6_k": ModelPreset(
        key="q6_k",
        name="Qwen 3.8 27B (Q6_K) - Near Lossless",
        repo_id="unsloth/Qwen3.8-27B-GGUF",
        filename="Qwen3.8-27B-Q6_K.gguf",
        estimated_size_gb=22.9,
        quant_type="6-bit K-Quant",
        min_ram_vram_gb=32.0,
        recommended_for="Workstations with 32 GB+ VRAM/RAM seeking 99.9% FP16 output matching.",
        description="6-bit high-precision weights virtually indistinguishable from unquantized FP16."
    ),
    "q8_0": ModelPreset(
        key="q8_0",
        name="Qwen 3.8 27B (Q8_0) - Studio Grade",
        repo_id="unsloth/Qwen3.8-27B-GGUF",
        filename="Qwen3.8-27B-Q8_0.gguf",
        estimated_size_gb=29.0,
        quant_type="8-bit Quantized",
        min_ram_vram_gb=40.0,
        recommended_for="Enterprise GPU servers and Mac Studio workstations.",
        description="Full 8-bit quantization offering maximum theoretical precision in quantized format."
    )
}

DEFAULT_PRESET = "q4_k_m"
DEFAULT_DESTINATION = os.path.expanduser("~/Models/Qwen3.8-27B-GGUF")


# =============================================================================
# 🛡️ Defensive Utilities & Hardware Auditing
# =============================================================================

class HardwareAuditor:
    """Audits local hardware (RAM, Swap, GPU) and estimates execution feasibility."""

    @staticmethod
    def inspect_system() -> Dict[str, Any]:
        info: Dict[str, Any] = {
            "total_ram_gb": 0.0,
            "available_ram_gb": 0.0,
            "swap_gb": 0.0,
            "has_nvidia_gpu": False,
            "gpu_details": []
        }

        if psutil:
            vmem = psutil.virtual_memory()
            smem = psutil.swap_memory()
            info["total_ram_gb"] = vmem.total / (1024 ** 3)
            info["available_ram_gb"] = vmem.available / (1024 ** 3)
            info["swap_gb"] = smem.total / (1024 ** 3)

        if shutil.which("nvidia-smi"):
            info["has_nvidia_gpu"] = True
            try:
                import subprocess
                res = subprocess.run(
                    ["nvidia-smi", "--query-gpu=name,memory.total,memory.free", "--format=csv,noheader,nounits"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if res.returncode == 0:
                    for line in res.stdout.strip().split("\n"):
                        if line:
                            parts = [p.strip() for p in line.split(",")]
                            if len(parts) >= 3:
                                info["gpu_details"].append({
                                    "name": parts[0],
                                    "total_vram_mb": float(parts[1]),
                                    "free_vram_mb": float(parts[2])
                                })
            except Exception:
                pass

        return info

    @classmethod
    def print_audit(cls, preset: ModelPreset):
        sys_info = cls.inspect_system()
        print("\n" + "=" * 70)
        print("🖥️  HARDWARE FEASIBILITY AUDIT")
        print("=" * 70)
        print(f"Target Model            : {preset.name}")
        print(f"Quantization            : {preset.quant_type}")
        print(f"Estimated Weights Size  : {preset.estimated_size_gb:.1f} GB")
        print(f"Recommended RAM/VRAM    : {preset.min_ram_vram_gb:.1f} GB")
        print("-" * 70)
        print(f"Detected System RAM     : {sys_info['total_ram_gb']:.2f} GB total ({sys_info['available_ram_gb']:.2f} GB available)")
        print(f"Detected Swap Space     : {sys_info['swap_gb']:.2f} GB")

        if sys_info["has_nvidia_gpu"] and sys_info["gpu_details"]:
            print("Detected NVIDIA GPU(s)  :")
            for idx, gpu in enumerate(sys_info["gpu_details"]):
                print(f"  [{idx}] {gpu['name']} - VRAM: {gpu['total_vram_mb']/1024:.2f} GB (Free: {gpu['free_vram_mb']/1024:.2f} GB)")
        else:
            print("Detected GPU            : No dedicated NVIDIA GPU detected (CPU/RAM inference mode).")

        print("-" * 70)
        if sys_info["total_ram_gb"] >= preset.min_ram_vram_gb:
            print("✅ Status: Current hardware can load and run this model locally.")
        else:
            print("⚠️  Status: Current hardware is below recommended threshold.")
            print(f"💡 Note  : The model weights can be downloaded and preserved on disk now.")
            print(f"          To run inference, load these weights on a system with {preset.min_ram_vram_gb:.1f} GB+ RAM/VRAM.")
        print("=" * 70 + "\n")


# =============================================================================
# 🚀 Download & Verification Engine
# =============================================================================

class ModelManager:
    """Defensive download and verification manager for local AI weights."""

    def __init__(self, destination_dir: str = DEFAULT_DESTINATION):
        self.dest_dir = Path(os.path.expanduser(destination_dir)).resolve()
        self._setup_signals()

    def _setup_signals(self):
        def _handle_interrupt(signum, frame):
            print("\n\n🛑 Operation cancelled by user. Safe exit initiated.")
            sys.exit(130)
        signal.signal(signal.SIGINT, _handle_interrupt)
        signal.signal(signal.SIGTERM, _handle_interrupt)

    def check_disk_safety(self, required_gb: float, safety_margin_gb: float = 2.0) -> bool:
        """Ensures destination disk partition has adequate free capacity."""
        self.dest_dir.mkdir(parents=True, exist_ok=True)
        usage = shutil.disk_usage(self.dest_dir)
        free_gb = usage.free / (1024 ** 3)
        total_needed = required_gb + safety_margin_gb

        print(f"📊 Disk Pre-flight Check for {self.dest_dir}:")
        print(f"   Available Free Space : {free_gb:.2f} GB")
        print(f"   Required (with buffer): {total_needed:.2f} GB ({required_gb:.2f} GB + {safety_margin_gb:.1f} GB margin)")

        if free_gb < total_needed:
            print(f"❌ ERROR: Insufficient disk space on target partition! Need {total_needed:.2f} GB, have {free_gb:.2f} GB.", file=sys.stderr)
            return False

        print("   ✅ Disk safety validation passed.")
        return True

    def download(self, preset_key: str = DEFAULT_PRESET, max_retries: int = 3) -> Optional[Path]:
        """Downloads the target model preset with auto-resume and retry logic."""
        if hf_hub_download is None:
            print("❌ ERROR: 'huggingface_hub' is not installed! Run: pip install huggingface_hub", file=sys.stderr)
            return None

        # Normalize key
        norm_key = preset_key.lower().replace("-", "_")
        if norm_key not in PRESETS:
            print(f"❌ Unknown preset '{preset_key}'.", file=sys.stderr)
            self.list_presets()
            return None

        preset = PRESETS[norm_key]
        HardwareAuditor.print_audit(preset)

        if not self.check_disk_safety(preset.estimated_size_gb):
            return None

        target_file = self.dest_dir / preset.filename
        print(f"🚀 Initiating Download for {preset.name}:")
        print(f"   Repository  : {preset.repo_id}")
        print(f"   GGUF File   : {preset.filename}")
        print(f"   Target Path : {target_file}")
        print(f"   Transfer    : Resumable HTTP Range Streaming\n")

        for attempt in range(1, max_retries + 1):
            try:
                start_time = time.time()
                downloaded_path = hf_hub_download(
                    repo_id=preset.repo_id,
                    filename=preset.filename,
                    local_dir=str(self.dest_dir),
                    local_dir_use_symlinks=False,
                    resume_download=True
                )
                elapsed = time.time() - start_time
                actual_path = Path(downloaded_path)
                file_size_gb = actual_path.stat().st_size / (1024 ** 3)

                print("\n" + "=" * 70)
                print("🎉 DOWNLOAD COMPLETED SUCCESSFULLY!")
                print(f"📦 File Path  : {actual_path}")
                print(f"📊 File Size  : {file_size_gb:.2f} GB")
                print(f"⏱️  Duration   : {elapsed:.1f} seconds")
                print("=" * 70 + "\n")
                return actual_path

            except Exception as exc:
                print(f"\n⚠️  Attempt {attempt}/{max_retries} failed: {exc}", file=sys.stderr)
                if attempt < max_retries:
                    wait_sec = attempt * 5
                    print(f"⏳ Retrying in {wait_sec} seconds...")
                    time.sleep(wait_sec)
                else:
                    print("❌ All download attempts exhausted. Please verify your internet connection.", file=sys.stderr)
                    return None

    def status(self):
        """Displays status of existing downloaded models in destination."""
        print("\n" + "=" * 70)
        print(f"📂 LOCAL MODEL INVENTORY ({self.dest_dir})")
        print("=" * 70)

        if not self.dest_dir.exists():
            print(f"Directory {self.dest_dir} does not exist yet.")
            return

        files = list(self.dest_dir.glob("*.gguf")) + list(self.dest_dir.glob("*.safetensors"))
        if not files:
            print("No model weight files (.gguf / .safetensors) found.")
        else:
            for f in sorted(files):
                size_gb = f.stat().st_size / (1024 ** 3)
                mtime = time.ctime(f.stat().st_mtime)
                print(f"• {f.name}")
                print(f"  Size: {size_gb:.2f} GB | Modified: {mtime}")
        print("=" * 70 + "\n")

    @staticmethod
    def list_presets():
        """Prints available preset table."""
        print("\n" + "=" * 70)
        print("📋 AVAILABLE UNSLOTH QWEN 3.8 GGUF PRESETS")
        print("=" * 70)
        for key, p in PRESETS.items():
            print(f"• {key:12s} : {p.name}")
            print(f"  File: {p.filename} | Size: ~{p.estimated_size_gb:.1f} GB | Min RAM: {p.min_ram_vram_gb:.1f} GB")
            print(f"  Use : {p.recommended_for}\n")
        print("=" * 70)


# =============================================================================
# 🖥️ CLI Entrypoint
# =============================================================================

def build_cli_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Unsloth Qwen 3.8 GGUF Model Lifecycle & Resilient Downloader",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download recommended Q4_K_M preset (~17.1 GB)
  python qwen3.8.py --download

  # Download high-precision Q5_K_M preset (~19.8 GB)
  python qwen3.8.py --download --preset q5_k_m

  # Download Unsloth Dynamic V3 UD-Q4_K_XL preset (~17.9 GB)
  python qwen3.8.py --download --preset ud_q4_k_xl

  # Download lightweight 3-bit preset (~13.8 GB for 16GB RAM)
  python qwen3.8.py --download --preset q3_k_m

  # List all available presets with sizes and hardware requirements
  python qwen3.8.py --list-presets

  # Check local downloaded model inventory
  python qwen3.8.py --status
        """
    )
    parser.add_argument(
        "--download", action="store_true",
        help="Initiate resumable download for target preset"
    )
    parser.add_argument(
        "--preset", type=str, default=DEFAULT_PRESET,
        choices=list(PRESETS.keys()),
        help=f"Select model preset (default: {DEFAULT_PRESET}). Options: {', '.join(PRESETS.keys())}"
    )
    parser.add_argument(
        "--dest", type=str, default=DEFAULT_DESTINATION,
        help=f"Target destination directory (default: {DEFAULT_DESTINATION})"
    )
    parser.add_argument(
        "--status", action="store_true",
        help="Display inventory of downloaded models in target directory"
    )
    parser.add_argument(
        "--audit", action="store_true",
        help="Audit hardware capabilities against model requirements without downloading"
    )
    parser.add_argument(
        "--list-presets", action="store_true",
        help="List all available quantization presets and details"
    )
    return parser


def main():
    parser = build_cli_parser()
    args = parser.parse_args()

    manager = ModelManager(destination_dir=args.dest)

    if args.list_presets:
        manager.list_presets()
    elif args.status:
        manager.status()
    elif args.audit:
        norm_key = args.preset.lower().replace("-", "_")
        preset = PRESETS.get(norm_key, PRESETS[DEFAULT_PRESET])
        HardwareAuditor.print_audit(preset)
    elif args.download:
        norm_key = args.preset.lower().replace("-", "_")
        manager.download(preset_key=norm_key)
    else:
        norm_key = args.preset.lower().replace("-", "_")
        preset = PRESETS.get(norm_key, PRESETS[DEFAULT_PRESET])
        HardwareAuditor.print_audit(preset)
        manager.status()
        print("💡 Tip: Run 'python qwen3.8.py --download' to download the recommended Q4_K_M model.")


if __name__ == "__main__":
    main()
