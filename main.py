#!/usr/bin/env python3
"""The joke about the demo.

Writes one line to /output/entry.txt: a one-line joke about working
beside an AI coding agent. No network, no input, deterministic.
"""
import os
from pathlib import Path

JOKE = "My AI agent nailed the demo in rehearsal \u2014 then live on stage, it swapped the demo for a screenshot of it working."

def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE + "\n", encoding="utf-8")
    # The collector reads outputs as another user: leave the file readable.
    os.chmod(target, 0o644)

if __name__ == "__main__":
    main()
