"""coolest-art-01 entry (Python 3.13, stdlib only): copy art.png to the output dir."""
import os
import shutil
from pathlib import Path

src = Path(__file__).resolve().parent / "art.png"
if not src.is_file():
    raise FileNotFoundError(f"art.png not found next to main.py: {src}")
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, out_dir / "entry.png")
