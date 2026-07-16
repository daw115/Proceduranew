#!/usr/bin/env python3
"""Buduje pojedynczy canvas A4 wyrażający filozofię „Mierzony Przepływ”."""
from __future__ import annotations

import hashlib
import math
import os
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, __version__ as PILLOW_VERSION, features

ROOT = Path(__file__).parent
OUT = ROOT / "IDCC_DESIGN_CANVAS_FINAL.png"
WIDTH, HEIGHT = 2480, 3508
SCALE = 2

PAPER = "#F3F0E8"
INK = "#132A43"
NAVY = "#173F63"
BLUE = "#1E668F"
MUTED = "#566672"
RULE = "#C9CED0"
RED = "#B72E2A"
AMBER = "#B97713"
GREEN = "#28704D"

EXPECTED_PILLOW_VERSION = "12.3.0"
EXPECTED_FREETYPE_VERSION = "2.14.3"
EXPECTED_FONT_SHA256 = "8b23d6341a12454e68e35c2c0917f0504104ded6aa3024d18e9d462da06fadd3"
# Ścieżkę do pinowanego kroju Noto Sans można nadpisać przez PROCEDURA_FONT_PATH;
# sha256 pliku musi się zgadzać niezależnie od lokalizacji (determinizm renderu).
FONT_PATH = Path(os.environ.get(
    "PROCEDURA_FONT_PATH", "/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf"))
if PILLOW_VERSION != EXPECTED_PILLOW_VERSION:
    raise RuntimeError(
        f"Budowa canvasu wymaga Pillow {EXPECTED_PILLOW_VERSION}; wykryto {PILLOW_VERSION}")
if features.version_module("freetype2") != EXPECTED_FREETYPE_VERSION:
    raise RuntimeError(
        "Budowa canvasu wymaga FreeType "
        f"{EXPECTED_FREETYPE_VERSION}; wykryto {features.version_module('freetype2')}")
if not FONT_PATH.exists():
    raise FileNotFoundError(
        f"Brak kroju Noto Sans wymaganego do budowy canvasu: {FONT_PATH}\n"
        "Pobierz wariantywny plik NotoSans[wght].ttf (pakiet google-noto-vf) "
        "i wskaż go zmienną środowiskową PROCEDURA_FONT_PATH; sha256 pliku musi "
        f"wynosić {EXPECTED_FONT_SHA256}.")
font_digest = hashlib.sha256(FONT_PATH.read_bytes()).hexdigest()
if font_digest != EXPECTED_FONT_SHA256:
    raise RuntimeError(
        f"Niezgodny plik Noto Sans: {font_digest}; oczekiwano {EXPECTED_FONT_SHA256}")


def font(size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_PATH), size * SCALE)


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, size: int,
         fill: str = INK, anchor: str | None = None, spacing: int = 4) -> None:
    draw.text((xy[0] * SCALE, xy[1] * SCALE), value, font=font(size), fill=fill,
              anchor=anchor, spacing=spacing * SCALE)


def line(draw: ImageDraw.ImageDraw, points: list[tuple[float, float]], fill: str,
         width: int = 1) -> None:
    draw.line([(int(x * SCALE), int(y * SCALE)) for x, y in points], fill=fill,
              width=max(1, width * SCALE), joint="curve")


def rectangle(draw: ImageDraw.ImageDraw, box: tuple[float, float, float, float],
              fill: str | None = None, outline: str | None = None, width: int = 1) -> None:
    draw.rectangle(tuple(int(v * SCALE) for v in box), fill=fill, outline=outline,
                   width=max(1, width * SCALE))


def ellipse(draw: ImageDraw.ImageDraw, box: tuple[float, float, float, float],
            fill: str | None = None, outline: str | None = None, width: int = 1) -> None:
    draw.ellipse(tuple(int(v * SCALE) for v in box), fill=fill, outline=outline,
                 width=max(1, width * SCALE))


def arc(draw: ImageDraw.ImageDraw, box: tuple[float, float, float, float], start: int,
        end: int, fill: str, width: int) -> None:
    draw.arc(tuple(int(v * SCALE) for v in box), start=start, end=end, fill=fill,
             width=max(1, width * SCALE))


def draw_custom_idcc(draw: ImageDraw.ImageDraw, x: int, y: int, height: int) -> None:
    """Rysuje autorskie, geometryczne litery zamiast gotowego kroju display."""
    stroke = 18
    width_i = 56
    width_letter = 168
    gap = 52
    line(draw, [(x + width_i / 2, y), (x + width_i / 2, y + height)], INK, stroke)
    cursor = x + width_i + gap
    line(draw, [(cursor + width_letter, y), (cursor + 44, y), (cursor, y + 44),
                (cursor, y + height - 44), (cursor + 44, y + height),
                (cursor + width_letter, y + height)], INK, stroke)
    cursor += width_letter + gap
    for _ in range(2):
        line(draw, [(cursor + width_letter, y), (cursor + 44, y), (cursor, y + 44),
                    (cursor, y + height - 44), (cursor + 44, y + height),
                    (cursor + width_letter, y + height)], INK, stroke)
        cursor += width_letter + gap


def build() -> None:
    image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), PAPER)
    draw = ImageDraw.Draw(image)
    margin = 190
    right = WIDTH - margin

    # Rama i punkty rejestracyjne.
    rectangle(draw, (margin, margin, right, HEIGHT - margin), outline=INK, width=2)
    for x, y in ((margin, margin), (right, margin), (margin, HEIGHT - margin),
                 (right, HEIGHT - margin)):
        line(draw, [(x - 16, y), (x + 16, y)], RED, 2)
        line(draw, [(x, y - 16), (x, y + 16)], RED, 2)

    text(draw, (margin + 2, 240), "OPERATIONAL FIELD / 07", 19, MUTED)
    text(draw, (right - 2, 240), "CORE · TSO", 19, MUTED, anchor="ra")
    draw_custom_idcc(draw, margin, 360, 310)
    text(draw, (margin + 4, 730), "MIERZONY PRZEPŁYW", 26, NAVY)
    line(draw, [(margin, 810), (right, 810)], INK, 2)
    line(draw, [(margin, 830), (margin + 510, 830)], RED, 7)

    # Pięć pól A–E: konstrukcja całej kompozycji.
    field_top, field_bottom = 980, 2790
    field_left, field_right = margin, right
    columns = 5
    column_width = (field_right - field_left) / columns
    group_labels = ("A", "B", "C", "D", "E")
    group_colors = (MUTED, BLUE, NAVY, AMBER, RED)
    for index in range(columns + 1):
        x = field_left + index * column_width
        line(draw, [(x, field_top), (x, field_bottom)], RULE, 1)
    for index, label in enumerate(group_labels):
        x = field_left + index * column_width
        text(draw, (int(x + 18), field_top - 54), label, 22, group_colors[index])
        rectangle(draw, (x + 18, field_top - 14, x + column_width - 18, field_top - 8),
                  fill=group_colors[index])

    # Osiemnaście torów i 309 punktów — dyskretna, nieopisana referencja.
    tracks = 18
    track_gap = (field_bottom - field_top) / tracks
    for row in range(tracks):
        y = field_top + track_gap * (row + 0.5)
        opacity_color = RULE if row % 3 else MUTED
        line(draw, [(field_left + 18, y), (field_right - 18, y)], opacity_color, 1)
        text(draw, (field_left - 22, int(y)), f"{row + 1:02d}", 12, MUTED, anchor="rm")

    random.seed(30915019)
    nodes: list[tuple[float, float, int]] = []
    for node_index in range(309):
        row = node_index % tracks
        jitter = random.uniform(-0.28, 0.28) * track_gap
        x = random.uniform(field_left + 34, field_right - 34)
        y = field_top + track_gap * (row + 0.5) + jitter
        radius = 2 if node_index % 11 else 4
        nodes.append((x, y, radius))
    nodes.sort(key=lambda item: (item[1], item[0]))
    for index, (x, y, radius) in enumerate(nodes):
        color = RED if index in (24, 39, 149, 308) else NAVY if index % 7 else BLUE
        ellipse(draw, (x - radius, y - radius, x + radius, y + radius), fill=color)

    # Cztery okna obliczeniowe i proporcja 40/25 jako warstwa ukrytej geometrii.
    cx, cy = 1835, 2070
    radii = (350, 282, 214, 146)
    cycle_colors = (RULE, BLUE, NAVY, RED)
    for idx, radius in enumerate(radii):
        box = (cx - radius, cy - radius, cx + radius, cy + radius)
        arc(draw, box, -90, 270, cycle_colors[idx], 4 if idx < 3 else 7)
        angle = math.radians(-90 + (250 if idx == 3 else 40 + idx * 64))
        px, py = cx + radius * math.cos(angle), cy + radius * math.sin(angle)
        ellipse(draw, (px - 7, py - 7, px + 7, py + 7), fill=cycle_colors[idx])
    line(draw, [(cx - 430, cy), (cx + 430, cy)], PAPER, 20)
    line(draw, [(cx, cy - 430), (cx, cy + 430)], PAPER, 20)
    text(draw, (cx, cy - 28), "40", 72, INK, anchor="mm")
    text(draw, (cx, cy + 48), "25", 31, RED, anchor="mm")

    # Kliniczna stopka danych i spokojne domknięcie kompozycji.
    line(draw, [(margin, 2920), (right, 2920)], INK, 2)
    metrics = (("309", "OBSERWACJE"), ("150", "TABELE"), ("019", "WIADOMOŚCI"),
               ("A—E", "SYSTEM"))
    metric_width = (right - margin) / len(metrics)
    for index, (value, label) in enumerate(metrics):
        x = margin + index * metric_width
        if index:
            line(draw, [(x, 2955), (x, 3190)], RULE, 1)
        text(draw, (int(x + 22), 3008), value, 38, INK)
        text(draw, (int(x + 22), 3075), label, 13, MUTED)
    text(draw, (margin, 3265), "FORMA · PRZEPŁYW · DECYZJA", 15, NAVY)
    text(draw, (right, 3265), "M.01 / SKALIBROWANO", 15, MUTED, anchor="ra")

    # Ostateczna kontrola marginesów przed skalowaniem.
    bounds = image.getbbox()
    assert bounds == (0, 0, WIDTH * SCALE, HEIGHT * SCALE)
    image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS).save(OUT, optimize=True)
    with Image.open(OUT) as check:
        assert check.size == (WIDTH, HEIGHT) and check.mode == "RGB"
    print(f"Zapisano: {OUT} ({WIDTH} × {HEIGHT} px)")


if __name__ == "__main__":
    build()
