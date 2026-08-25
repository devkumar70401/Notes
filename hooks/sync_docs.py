import os
import shutil
from pathlib import Path

def on_pre_build(config):
    root_dir = Path(__file__).resolve().parent.parent
    docs_dir = root_dir / "docs"
    docs_dir.mkdir(exist_ok=True)
    
    # 1. Clean up broken symlinks in docs_dir
    for item in docs_dir.iterdir():
        if item.is_symlink() and not item.exists():
            item.unlink()

    # 2. Ensure docs/index.md exists
    index_md = docs_dir / "index.md"
    if not index_md.exists():
        index_md.write_text("# Hi, Brother 😊\n\nWelcome to my notes.\n", encoding="utf-8")
            
    # 3. Only link numbered directories that exist and contain actual files
    for item in root_dir.iterdir():
        if item.is_dir() and len(item.name) > 2 and item.name[:2].isdigit() and item.name[2] == "_":
            has_files = any(f.is_file() and not f.name.startswith(".") for f in item.rglob("*"))
            if has_files:
                target = docs_dir / item.name
                if not target.exists() and not target.is_symlink():
                    try:
                        target.symlink_to(f"../{item.name}")
                    except OSError:
                        if not target.exists():
                            shutil.copytree(item, target)

    # 4. Ensure assets, javascripts, stylesheets are copied to docs
    for folder in ["assets", "javascripts", "stylesheets"]:
        src_folder = root_dir / folder
        dst_folder = docs_dir / folder
        if src_folder.exists():
            dst_folder.mkdir(exist_ok=True)
            for f in src_folder.glob("*"):
                if f.is_file():
                    shutil.copy2(f, dst_folder / f.name)
