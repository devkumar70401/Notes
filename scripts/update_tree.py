#!/usr/bin/env python3
"""
Automated directory tree generator and injector for Notes/README.md.
Scans the Notes directory and updates the tree block at the end of README.md.

Usage:
    python3 update_tree.py          # Run once to update README.md
    python3 update_tree.py --watch  # Run in background to auto-update on changes
"""

import subprocess
import sys
import time
from pathlib import Path

def find_notes_root() -> Path:
    """Dynamically locate the Notes directory containing README.md."""
    # 1. Check command-line argument if explicitly provided
    for arg in sys.argv[1:]:
        if not arg.startswith("-"):
            p = Path(arg).resolve()
            if p.is_dir() and (p / "README.md").exists():
                return p

    # 2. Search upwards from script location
    script_dir = Path(__file__).resolve().parent
    for candidate in [script_dir] + list(script_dir.parents):
        if (candidate / "README.md").exists():
            return candidate

    # 3. Search upwards from current working directory
    cwd = Path.cwd().resolve()
    for candidate in [cwd] + list(cwd.parents):
        if (candidate / "README.md").exists():
            return candidate

    # Fallback to parent directory if in a subfolder like scripts/
    return script_dir.parent if script_dir.name in ("scripts", "tools", "bin") else script_dir


NOTES_DIR = find_notes_root()
README_FILE = NOTES_DIR / "README.md"

# Exclusion patterns
EXCLUDED_NAMES = {
    ".git",
    ".venv",
    ".cache",
    ".pytest_cache",
    "__pycache__",
    ".DS_Store",
    "update_tree.py",
    ".update_tree.py",
}

START_MARKER = "<!-- NOTES_TREE_START -->"
END_MARKER = "<!-- NOTES_TREE_END -->"


def build_tree_lines(dir_path: Path, prefix: str = "") -> list[str]:
    """Recursively generate an ASCII tree list of strings for directory contents."""
    try:
        entries = [
            item
            for item in dir_path.iterdir()
            if item.name not in EXCLUDED_NAMES
            and not item.name.startswith((".", "#", "~"))
            and not item.name.endswith(("~", ".swp", ".bak"))
        ]
    except PermissionError:
        return []

    # Sort directories first, then files alphabetically
    entries.sort(key=lambda x: (not x.is_dir(), x.name.lower()))
    lines = []

    for idx, entry in enumerate(entries):
        is_last = idx == len(entries) - 1
        connector = "└── " if is_last else "├── "
        child_prefix = "    " if is_last else "│   "

        if entry.is_dir():
            lines.append(f"{prefix}{connector}{entry.name}/")
            lines.extend(build_tree_lines(entry, prefix + child_prefix))
        else:
            lines.append(f"{prefix}{connector}{entry.name}")

    return lines


def generate_tree_block() -> str:
    """Capture the whole tree command output directly."""
    try:
        tree_output = subprocess.check_output(["tree"], cwd=NOTES_DIR, text=True).rstrip()
    except Exception:
        tree_lines = ["."]
        child_lines = build_tree_lines(NOTES_DIR)
        if child_lines:
            tree_lines.extend(child_lines)
        tree_output = "\n".join(tree_lines)

    return f"```text\n{tree_output}\n```"


def update_readme() -> bool:
    """Inject or replace the tree block between markers in README.md."""
    if not README_FILE.exists():
        print(f"Error: {README_FILE} does not exist.", file=sys.stderr)
        return False

    content = README_FILE.read_text(encoding="utf-8")
    tree_block = generate_tree_block()
    replacement = f"{START_MARKER}\n{tree_block}\n{END_MARKER}"

    if START_MARKER in content and END_MARKER in content:
        # Replace existing block
        start_idx = content.find(START_MARKER)
        end_idx = content.find(END_MARKER) + len(END_MARKER)
        new_content = content[:start_idx] + replacement + content[end_idx:]
    else:
        # Append section at the end
        new_content = (
            content.rstrip()
            + f"\n\n---\n\n## 📁 Part IV: Notes Directory Tree\n\n{replacement}\n"
        )

    if new_content != content:
        README_FILE.write_text(new_content, encoding="utf-8")
        print("✅ Successfully updated Notes directory tree in README.md")
        return True
    else:
        print("ℹ️ Tree is already up to date in README.md")
        return False


def get_dir_state() -> tuple:
    """Capture a snapshot of the directory structure to detect changes."""
    state = []
    for item in sorted(NOTES_DIR.rglob("*")):
        if any(part in EXCLUDED_NAMES or part.startswith(".") for part in item.parts):
            continue
        if item.name == "README.md":
            continue
        try:
            stat = item.stat()
            state.append((str(item.relative_to(NOTES_DIR)), stat.st_mtime, stat.st_size))
        except FileNotFoundError:
            pass
    return tuple(state)


def watch_mode():
    """Continuously watch for filesystem changes and update README.md."""
    print("👀 Watching Notes folder for changes (press Ctrl+C to exit)...")
    update_readme()
    last_state = get_dir_state()

    try:
        while True:
            time.sleep(2)
            current_state = get_dir_state()
            if current_state != last_state:
                print("🔄 Changes detected in Notes folder. Updating README.md...")
                update_readme()
                last_state = current_state
    except KeyboardInterrupt:
        print("\n👋 Stopped watcher.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("--watch", "-w"):
        watch_mode()
    else:
        update_readme()
