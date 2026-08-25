import os
import shutil
from pathlib import Path

def on_pre_build(config):
    root_dir = Path(__file__).resolve().parent.parent
    docs_dir = root_dir / "docs"
    docs_dir.mkdir(exist_ok=True)
    
    # 1. Link or copy README.md to docs/index.md
    index_md = docs_dir / "index.md"
    readme = root_dir / "README.md"
    if readme.exists():
        if index_md.is_symlink() or index_md.exists():
            try:
                index_md.unlink(missing_ok=True)
            except OSError:
                pass
        try:
            index_md.symlink_to("../README.md")
        except OSError:
            shutil.copy2(readme, index_md)
            
    # 2. Link all [0-9][0-9]_* numbered domain directories
    for item in root_dir.iterdir():
        if item.is_dir() and len(item.name) > 2 and item.name[:2].isdigit() and item.name[2] == "_":
            target = docs_dir / item.name
            if not target.exists() and not target.is_symlink():
                try:
                    target.symlink_to(f"../{item.name}")
                except OSError:
                    if not target.exists():
                        shutil.copytree(item, target)

    # 3. Ensure javascripts are available
    src_js = root_dir / "javascripts"
    dst_js = docs_dir / "javascripts"
    if src_js.exists():
        dst_js.mkdir(exist_ok=True)
        for js_file in src_js.glob("*.js"):
            shutil.copy2(js_file, dst_js / js_file.name)
