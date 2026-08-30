import os
import shutil
from pathlib import Path

def sync_all(root_dir, docs_dir):
    docs_dir.mkdir(exist_ok=True)
    
    # 1. Clean up stale or broken symlinks/dirs in docs_dir
    valid_names = {item.name for item in root_dir.iterdir() if not item.name.startswith(".")}
    valid_names.update({"index.md", "assets", "javascripts", "stylesheets"})
    for item in docs_dir.iterdir():
        if item.name not in valid_names or (item.is_symlink() and not item.exists()):
            if item.is_symlink() or item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)

    # 2. Ensure docs/index.md exists
    index_md = docs_dir / "index.md"
    if not index_md.exists() and not (root_dir / "README.md").exists():
        index_md.write_text("# Hi, Brother 😊\n\nWelcome to my notes.\n", encoding="utf-8")
    elif (root_dir / "README.md").exists() and not index_md.exists() and not index_md.is_symlink():
        try:
            index_md.symlink_to("../README.md")
        except OSError:
            shutil.copy2(root_dir / "README.md", index_md)
            
    # 3. Link top-level content directories
    excluded_dirs = {
        "docs", "site", ".venv", ".git", ".github", ".cache",
        "__pycache__", "hooks", "assets", "javascripts", "stylesheets"
    }
    for item in root_dir.iterdir():
        if item.is_dir() and item.name not in excluded_dirs and not item.name.startswith("."):
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

def on_config(config):
    root_dir = Path(__file__).resolve().parent.parent
    docs_dir = root_dir / ".docs"
    sync_all(root_dir, docs_dir)
    return config

def on_pre_build(config):
    root_dir = Path(__file__).resolve().parent.parent
    docs_dir = root_dir / ".docs"
    sync_all(root_dir, docs_dir)

