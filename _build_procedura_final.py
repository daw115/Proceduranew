#!/usr/bin/env python3
"""Buduje czyste wydanie finalnego składu bez nadpisywania źródłowej wersji v7."""
from __future__ import annotations

import hashlib
import os
import runpy
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE_HTML = ROOT / "PROCEDURA_IDCC_TSO_v7.html"
SOURCE_STICKERS = ROOT / "STICKERY_IDCC.md"
FINAL_HTML = ROOT / "PROCEDURA_IDCC_TSO_v7-final.html"
FINAL_STICKERS = ROOT / "STICKERY_IDCC-final.md"


def digest(path: Path) -> str | None:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def main() -> None:
    protected_before = {
        SOURCE_HTML: digest(SOURCE_HTML),
        SOURCE_STICKERS: digest(SOURCE_STICKERS),
    }
    os.environ.update({
        "PROCEDURA_OUTPUT": FINAL_HTML.name,
        "PROCEDURA_STICKERS_OUTPUT": FINAL_STICKERS.name,
        "PROCEDURA_LAYOUT": "measured-flow",
        "PROCEDURA_INCLUDE_COMMENTS": "0",
    })
    runpy.run_path(str(ROOT / "_build_design_canvas.py"), run_name="__main__")
    runpy.run_path(str(ROOT / "_build_procedura_v7.py"), run_name="__main__")

    for path, expected in protected_before.items():
        if digest(path) != expected:
            raise RuntimeError(f"Finalny build naruszył chroniony plik źródłowy: {path.name}")
    if not FINAL_HTML.is_file() or not FINAL_STICKERS.is_file():
        raise RuntimeError("Finalny build nie utworzył wszystkich oczekiwanych artefaktów")
    print(f"Źródła zachowane bez zmian; finalny dokument: {FINAL_HTML}")


if __name__ == "__main__":
    main()
