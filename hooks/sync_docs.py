import os
import shutil
from pathlib import Path

def sync_all(root_dir: Path, docs_dir: Path):
    docs_dir.mkdir(exist_ok=True)

    excluded_dirs = {
        "docs", ".docs", "site", ".venv", ".git", ".github", ".cache",
        "__pycache__", "hooks", "assets", "javascripts", "stylesheets",
        ".vscode", "tmp"
    }

    # 1. Clean up stale or broken symlinks / items in docs_dir
    valid_names = {
        item.name for item in root_dir.iterdir()
        if not item.name.startswith(".") and item.name not in excluded_dirs
    }
    valid_names.update({"index.md", ".pages", "assets", "javascripts", "stylesheets"})

    if docs_dir.exists():
        for item in docs_dir.iterdir():
            if item.name not in valid_names or item.name in excluded_dirs or (item.is_symlink() and not item.exists()):
                if item.is_symlink() or item.is_file():
                    item.unlink()
                elif item.is_dir():
                    shutil.rmtree(item)

    # 2. Ensure docs/index.md and docs/.pages exist
    root_pages = root_dir / ".pages"
    docs_pages = docs_dir / ".pages"
    if root_pages.exists():
        try:
            if docs_pages.is_symlink() or docs_pages.exists():
                docs_pages.unlink()
            docs_pages.symlink_to("../.pages")
        except OSError:
            shutil.copy2(root_pages, docs_pages)

    index_md = docs_dir / "index.md"
    readme = root_dir / "README.md"
    if readme.exists():
        if index_md.is_symlink() or index_md.exists():
            index_md.unlink()
        try:
            index_md.symlink_to("../README.md")
        except OSError:
            shutil.copy2(readme, index_md)
    elif not index_md.exists():
        index_md.write_text("# Machine Learning Vault\n\nWelcome to the knowledge base.\n", encoding="utf-8")

    # 3. Link top-level content directories that contain markdown files
    for item in root_dir.iterdir():
        if item.is_dir() and item.name not in excluded_dirs and not item.name.startswith("."):
            has_md = any(f.is_file() and f.suffix == ".md" for f in item.rglob("*"))
            target = docs_dir / item.name
            if has_md:
                if not target.exists() and not target.is_symlink():
                    try:
                        target.symlink_to(f"../{item.name}")
                    except OSError:
                        if not target.exists():
                            shutil.copytree(item, target)
            else:
                if target.is_symlink() or target.is_file():
                    target.unlink()
                elif target.is_dir():
                    shutil.rmtree(target)

    # 4. Ensure assets, javascripts, stylesheets are copied/linked to docs
    for folder in ["assets", "javascripts", "stylesheets"]:
        src_folder = root_dir / folder
        dst_folder = docs_dir / folder
        if src_folder.exists():
            dst_folder.mkdir(exist_ok=True)
            for f in src_folder.glob("*"):
                if f.is_file():
                    dst_file = dst_folder / f.name
                    if dst_file.exists() or dst_file.is_symlink():
                        dst_file.unlink()
                    try:
                        dst_file.symlink_to(f"../../{folder}/{f.name}")
                    except OSError:
                        shutil.copy2(f, dst_file)

def on_config(config):
    root_dir = Path(__file__).resolve().parent.parent
    docs_dir = root_dir / ".docs"
    sync_all(root_dir, docs_dir)
    return config

def on_pre_build(config):
    root_dir = Path(__file__).resolve().parent.parent
    docs_dir = root_dir / ".docs"
    sync_all(root_dir, docs_dir)
