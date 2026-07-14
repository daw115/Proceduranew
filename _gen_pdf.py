#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert PROCEDURA_IDCC_TSO_v6.html to PDF using fpdf2."""
import re, os
from pathlib import Path
from fpdf import FPDF

import sys
_name = sys.argv[1] if len(sys.argv) > 1 else "PROCEDURA_IDCC_TSO_v6"
HTML = Path(__file__).parent / f"{_name}.html"
OUT = Path(__file__).parent / f"output/{_name}.pdf"

def _font_set():
    """Zwraca ścieżki fontów (regular, bold, italic, bold-italic) per platforma."""
    win = Path("C:/Windows/Fonts")
    mac = Path("/System/Library/Fonts/Supplemental")
    if (win / "calibri.ttf").exists():
        return [win/"calibri.ttf", win/"calibrib.ttf", win/"calibrii.ttf", win/"calibriz.ttf"]
    if (mac / "Arial.ttf").exists():
        return [mac/"Arial.ttf", mac/"Arial Bold.ttf", mac/"Arial Italic.ttf", mac/"Arial Bold Italic.ttf"]
    raise SystemExit("Brak fontów Calibri/Arial — uzupełnij _font_set().")
_F = _font_set()

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self._in_table = False
        self._table_rows = []
        self._table_cols = None
        # Calibri has better Unicode/Polish support than Arial
        self.add_font("Calibri", "", str(_F[0]))
        self.add_font("Calibri", "B", str(_F[1]))
        self.add_font("Calibri", "I", str(_F[2]))
        self.add_font("Calibri", "BI", str(_F[3]))

    def add_heading(self, text, level=1):
        self.ln(2)
        if level == 1:
            self.set_font("Calibri", "B", 16)
            self.set_text_color(30, 60, 120)
        elif level == 2:
            self.set_font("Calibri", "B", 14)
            self.set_text_color(40, 70, 140)
        elif level == 3:
            self.set_font("Calibri", "B", 12)
            self.set_text_color(50, 80, 150)
        elif level == 4:
            self.set_font("Calibri", "B", 11)
            self.set_text_color(60, 90, 160)
        self.multi_cell(0, 6, text)
        self.ln(2)
        self.set_text_color(0, 0, 0)

    def add_para(self, text, size=10):
        self.set_font("Calibri", "", size)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def add_bold_text(self, text, size=10):
        self.set_font("Calibri", "B", size)
        self.write(5.5, text)
        self.set_font("Calibri", "", size)

    def add_code(self, text):
        self.set_font("Courier", "", 9)
        self.multi_cell(0, 5, text)
        self.ln(1)
        self.set_font("Calibri", "", 10)

    def start_table(self, num_cols):
        self._in_table = True
        self._table_cols = num_cols
        self._table_rows = []

    def add_table_row(self, cells, is_header=False):
        self._table_rows.append((cells, is_header))

    def finish_table(self):
        if not self._table_rows:
            self._in_table = False
            return
        col_width = (self.w - 2 * self.l_margin) / self._table_cols
        for cells, _ in self._table_rows:
            max_h = max(len(cell) // 30 + 1 for cell in cells) * 4
        max_row_height = max(6, max_h) if self._table_rows else 6
        x_start = self.l_margin
        y_start = self.get_y()
        for cells, is_header in self._table_rows:
            if is_header:
                self.set_font("Calibri", "B", 8)
                self.set_fill_color(230, 235, 245)
            else:
                self.set_font("Calibri", "", 8)
                self.set_fill_color(255, 255, 255)
            for ci, cell in enumerate(cells):
                x = x_start + ci * col_width
                w = col_width - 1
                if self.get_y() + max_row_height > self.h - self.b_margin:
                    self.add_page()
                    y_start = self.get_y()
                self.rect(x, y_start, w, max_row_height)
                self.set_xy(x + 2, y_start + 1)
                self.multi_cell(w - 4, 3.5, cell, fill=False)
                self.set_xy(x_start, y_start + max_row_height)
            y_start += max_row_height
        self.set_y(y_start + 2)
        self._in_table = False
        self.ln(4)

    def add_horizontal_rule(self):
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)
        self.set_line_width(0.5)

    def add_list_item(self, text, indent=15):
        self.set_font("Calibri", "", 10)
        x = self.get_x()
        self.set_x(x + indent)
        self.write(5.5, chr(8226) + " " + text)
        self.ln()

    def add_note(self, text):
        self.set_fill_color(255, 255, 200)
        self.set_draw_color(200, 200, 100)
        y = self.get_y()
        self.rect(self.l_margin, y, self.w - self.l_margin - self.r_margin, 8, style='DF')
        self.set_xy(self.l_margin + 4, y + 1)
        self.set_font("Calibri", "", 9)
        self.multi_cell(self.w - self.l_margin - self.r_margin - 8, 5, text)
        self.set_y(y + 10)
        self.ln(2)


def parse_html_to_elements(html_text):
    elements = []
    html_text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html_text, flags=re.S)
    html_text = re.sub(r'<(meta|link|img)[^>]*/?>', '', html_text, flags=re.I)
    html_text = re.sub(r'\s+class="[^"]*"', '', html_text)
    html_text = re.sub(r'\s+id="[^"]*"', '', html_text)
    html_text = html_text.replace('&nbsp;', ' ')
    html_text = html_text.replace('&amp;', '&')
    html_text = html_text.replace('&lt;', '<')
    html_text = html_text.replace('&gt;', '>')
    html_text = html_text.replace('&quot;', '"')
    html_text = html_text.replace('&#39;', "'")

    parts = re.split(r'(</?(?:h[1-6]|p|table|thead|tbody|tr|td|th|ul|ol|li|blockquote|hr|div|pre|figure|figcaption)[^>]*>)', html_text)

    i = 0
    while i < len(parts):
        p = parts[i]

        m = re.match(r'<h([1-6])(?:\s+[^>]*)?>(.*?)</h\1>', p, re.S)
        if m:
            level = int(m.group(1))
            text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            if text:
                elements.append(('heading', level, text))
            i += 1
            continue

        m = re.match(r'<p(?:\s+[^>]*)?>(.*?)</p>', p, re.S)
        if m:
            text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            if text:
                elements.append(('para', text))
            i += 1
            continue

        if re.match(r'<hr(?:\s+/)?>', p, re.I):
            elements.append(('hr',))
            i += 1
            continue

        m = re.match(r'<table[^>]*>(.*?)</table>', p, re.S)
        if m:
            table_text = m.group(1)
            rows = re.findall(r'<tr[^>]*>(.*?)</tr>', table_text, re.S)
            if rows:
                elements.append(('table_start',))
                for row in rows:
                    cells = re.findall(r'<(td|th)[^>]*>(.*?)</\1>', row, re.S)
                    row_cells = [re.sub(r'<[^>]+>', '', c[1]).strip() for c in cells]
                    is_header = cells[0][0] == 'th' if cells else False
                    if row_cells:
                        elements.append(('table_row', row_cells, is_header))
                elements.append(('table_end',))
            i += 1
            continue

        m = re.match(r'<(ul|ol)[^>]*>(.*?)</\2>', p, re.S)
        if m:
            list_text = m.group(2)
            items = re.findall(r'<li[^>]*>(.*?)</li>', list_text, re.S)
            for item in items:
                text = re.sub(r'<[^>]+>', '', item).strip()
                if text:
                    elements.append(('list_item', text))
            i += 1
            continue

        m = re.match(r'<(b|strong|i|em)[^>]*>(.*?)</\1>', p, re.S)
        if m:
            tag = m.group(1)
            text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            if text:
                elements.append(('formatted', text, tag in ('b', 'strong')))
            i += 1
            continue

        m = re.match(r'<pre[^>]*>(.*?)</pre>', p, re.S)
        if m:
            text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
            if text:
                elements.append(('code', text))
            i += 1
            continue

        text = re.sub(r'\s+', ' ', p).strip()
        if text and text not in ('\n', ' ', ''):
            if not re.match(r'^<[a-z]', text, re.I):
                elements.append(('text', text))

        i += 1

    return elements


def _safe_multi_cell(pdf, text, h=5.5):
    """Render text, skipping if it contains unrenderable characters."""
    try:
        pdf.multi_cell(0, h, text)
    except Exception:
        # Strip problematic characters and retry
        cleaned = re.sub(r'[^\x00-\x7FĀ-ſ -⁯]', ' ', text)
        try:
            pdf.multi_cell(0, h, cleaned)
        except Exception:
            pass  # Skip entirely if still broken


def generate_pdf(elements):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    for elem in elements:
        etype = elem[0]
        if etype == 'heading':
            _, level, text = elem
            pdf.ln(2)
            if level == 1:
                pdf.set_font("Calibri", "B", 16)
                pdf.set_text_color(30, 60, 120)
            elif level == 2:
                pdf.set_font("Calibri", "B", 14)
                pdf.set_text_color(40, 70, 140)
            elif level == 3:
                pdf.set_font("Calibri", "B", 12)
                pdf.set_text_color(50, 80, 150)
            elif level == 4:
                pdf.set_font("Calibri", "B", 11)
                pdf.set_text_color(60, 90, 160)
            pdf.multi_cell(0, 6, text)
            pdf.ln(2)
            pdf.set_text_color(0, 0, 0)
        elif etype == 'para':
            pdf.set_font("Calibri", "", 10)
            _safe_multi_cell(pdf, elem[1])
            pdf.ln(1)
        elif etype == 'text':
            text = elem[1]
            if '**' in text:
                parts = text.split('**')
                for j, part in enumerate(parts):
                    if j % 2 == 1:
                        pdf.set_font("Calibri", "B", 10)
                        pdf.write(5.5, part)
                        pdf.set_font("Calibri", "", 10)
                    else:
                        pdf.set_font("Calibri", "", 10)
                        _safe_multi_cell(pdf, part)
            else:
                pdf.set_font("Calibri", "", 10)
                _safe_multi_cell(pdf, text)
        elif etype == 'hr':
            pdf.add_horizontal_rule()
        elif etype == 'table_start':
            pass
        elif etype == 'table_row':
            _, cells, is_header = elem
            pdf.add_table_row(cells, is_header)
        elif etype == 'table_end':
            pdf.finish_table()
        elif etype == 'list_item':
            pdf.add_list_item(elem[1])
        elif etype == 'formatted':
            _, text, is_bold = elem
            if is_bold:
                pdf.add_bold_text(text)
            else:
                pdf.set_font("Calibri", "", 10)
                _safe_multi_cell(pdf, text)
        elif etype == 'code':
            pdf.add_code(elem[1])
        elif etype == 'note':
            pdf.add_note(elem[1])

    return pdf


if __name__ == '__main__':
    OUT.parent.mkdir(exist_ok=True)
    html_text = HTML.read_text(encoding='utf-8')
    elements = parse_html_to_elements(html_text)
    print(f"Parsed {len(elements)} elements from HTML")

    pdf = generate_pdf(elements)
    pdf.output(str(OUT))
    print(f"PDF saved: {OUT} ({os.path.getsize(OUT)} bytes)")
