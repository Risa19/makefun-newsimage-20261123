"""news-image-20261123: write the entry image to /output/entry.png.

The image is a newspaper front page summing up world news of Monday
23 November 2026: NATO AWACS jets to Poland after Russian missiles
landed there, COP31 collapsing with no deal, Ukraine sinking a Russian
warship off Libya with naval drones, and Bitcoin falling to $55K then
rebounding to $61K.

Deterministic: a plain byte copy, so repeated runs write identical bytes.
"""

import os
import shutil
from pathlib import Path

SRC = Path(__file__).resolve().parent / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    os.makedirs(DST.parent, exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Fail loudly instead of shipping a truncated image.
    assert DST.stat().st_size == SRC.stat().st_size, "copy size mismatch"


if __name__ == "__main__":
    main()
