from __future__ import annotations

"""Post-build script for finance pack."""

import os
import shutil
from pathlib import Path


def copy_package_files():
    """Copy package.json and other metadata to dist."""
    root = Path(__file__).parent.parent
    dist = root / "dist"
    
    if not dist.exists():
        print("Dist directory not found, skipping post-build")
        return
    
    files_to_copy = ["package.json", "README.md"]
    
    for filename in files_to_copy:
        src = root / filename
        if src.exists():
            dst = dist / filename
            shutil.copy2(src, dst)
            print(f"Copied {filename} to dist/")


def main():
    """Run post-build tasks."""
    print("Running post-build tasks...")
    copy_package_files()
    print("Post-build complete!")


if __name__ == "__main__":
    main()
