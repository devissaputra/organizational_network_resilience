#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

INK = "#172033"
SOFT = "#475569"
GRAY = "#64748b"
GRID = "#e2e8f0"
TARGET = "#dc2626"
RANDOM = "#2563eb"
BAND = "#bfdbfe"
GREEN = "#16a34a"
PURPLE = "#7c3aed"
GOLD = "#f59e0b"
CYAN = "#0891b2"


def esc(value):
    return html.escape(str(value))


def text(x, y, value, size=16, weight="400", anchor="start", fill=INK):
    return (
        f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">'
        f'{esc(value)}</text>'
    )


def line(x1, y1, x2, y2, stroke=GRID, width=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{stroke}" stroke-width="{width}"{extra}/>'
    )


def box(x, y, width, height, title, body, fill, stroke, title_fill=INK):
    output = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="15" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>',
        text(x + 18, y + 31, title, 16, "700", "start", title_fill),
    ]
    for index, value in enumerate(body):
        output.append(
            text(x + 18, y + 57 + index * 21, value, 12.5, "400", "start", SOFT)
        )
    return "".join(output)


def arrow(x1, y1, x2, y2, color=GRAY):
    return (
        line(x1, y1, x2 - 12, y2, color, 2)
        + f'<polygon points="{x2-12},{y2-6} {x2},{y2} {x2-12},{y2+6}" fill="{color}"/>'
    )


def read_curve():
    with (ROOT / "data/derived/primary_results.csv").open(
        newline="", encoding="utf-8"
    ) as handle:
        return list(csv.DictReader(handle))


def research_design(rows):
    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        text(55, 50, "Communication-network resilience under actor loss", 30, "700"),
        text(
            55,
            80,
            "Static degree-targeted removal versus 200 version-stable comparator draws",
            15,
            "400",
            "start",
            SOFT,
        ),
    ]

    left, right, top, bottom = 105, 850, 130, 585
    xmin, xmax, ymin, ymax = 5, 30, 0.84, 1.04

    def sx(value):
        return left + (value - xmin) / (xmax - xmin) * (right - left)

    def sy(value):
        return bottom - (value - ymin) / (ymax - ymin) * (bottom - top)

    for value in (0.85, 0.90, 0.95, 1.00):
        y = sy(value)
        output.extend(
            [
                line(left, y, right, y),
                text(left - 14, y + 5, f"{value:.2f}", 12, "400", "end", GRAY),
            ]
        )

    for row in rows:
        x = sx(float(row["removed"]))
        output.extend(
            [
                line(x, top, x, bottom, "#f1f5f9"),
                text(x, bottom + 30, row["removed"], 12, "600", "middle", GRAY),
            ]
        )

    upper = " ".join(
        f'{sx(float(row["removed"]))},{sy(float(row["random_p95"]))}'
        for row in rows
    )
    lower = " ".join(
        f'{sx(float(row["removed"]))},{sy(float(row["random_p05"]))}'
        for row in reversed(rows)
    )
    output.append(
        f'<polygon points="{upper} {lower}" fill="{BAND}" fill-opacity="0.45" stroke="none"/>'
    )

    random_points = " ".join(
        f'{sx(float(row["removed"]))},{sy(float(row["random_mean"]))}'
        for row in rows
    )
    targeted_points = " ".join(
        f'{sx(float(row["removed"]))},{sy(float(row["targeted_retained_efficiency"]))}'
        for row in rows
    )

    output.extend(
        [
            f'<polyline points="{random_points}" fill="none" stroke="{RANDOM}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
            f'<polyline points="{targeted_points}" fill="none" stroke="{TARGET}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>',
        ]
    )

    for row in rows:
        x = sx(float(row["removed"]))
        y_target = sy(float(row["targeted_retained_efficiency"]))
        y_random = sy(float(row["random_mean"]))
        output.extend(
            [
                f'<circle cx="{x}" cy="{y_target}" r="6.5" fill="#fff" stroke="{TARGET}" stroke-width="3"/>',
                f'<circle cx="{x}" cy="{y_random}" r="6.5" fill="#fff" stroke="{RANDOM}" stroke-width="3"/>',
            ]
        )

    output.extend(
        [
            line(left, bottom, right, bottom, "#334155", 1.7),
            line(left, top, left, bottom, "#334155", 1.7),
            text((left + right) / 2, 660, "Actors removed", 14, "600", "middle"),
            f'<text x="28" y="{(top+bottom)/2}" transform="rotate(-90 28 {(top+bottom)/2})" '
            'font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="600" '
            f'text-anchor="middle" fill="{INK}">Retained global efficiency</text>',
            '<rect x="900" y="125" width="245" height="155" rx="15" fill="#f8fafc" stroke="#cbd5e1"/>',
            line(925, 160, 965, 160, TARGET, 4),
            text(980, 165, "Targeted", 12.5, "700"),
            line(925, 195, 965, 195, RANDOM, 4),
            text(980, 200, "Comparator mean", 12.5, "700"),
            f'<rect x="925" y="222" width="40" height="16" fill="{BAND}" fill-opacity="0.7"/>',
            text(980, 235, "Comparator p05–p95", 12.5, "700"),
            '<rect x="900" y="310" width="245" height="275" rx="15" fill="#fff7ed" stroke="#fdba74"/>',
            text(925, 342, "k = 30 stress point", 15, "700", "start", "#9a3412"),
            text(925, 374, "30 of 148 actors = 20.3%", 12.5, "600", "start", "#7c2d12"),
            text(925, 405, "Targeted retained", 12, "600", "start", "#7c2d12"),
            text(925, 428, "0.8608", 24, "700", "start", TARGET),
            text(925, 462, "Comparator mean", 12, "600", "start", "#7c2d12"),
            text(925, 485, "0.9917", 24, "700", "start", RANDOM),
            text(925, 520, "Gap = 0.1309", 14, "700", "start", "#7c2d12"),
            text(925, 550, "Targeted stays below comparator p05", 11.5, "600", "start", "#7c2d12"),
            text(925, 570, "at all five released stress levels.", 11.5, "600", "start", "#7c2d12"),
            text(55, 704, "The blue band is an deterministic pseudo-random comparator band, not a confidence interval. Email connectivity is a structural proxy for potential information access.", 12, "400", "start", GRAY),
            "</svg>",
        ]
    )

    return "".join(output)


def method():
    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="720" viewBox="0 0 1200 720">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        text(55, 50, "Reproducible resilience analysis pipeline", 30, "700"),
        text(
            55,
            80,
            "Source hypergraph → simple projection → stress test → comparator → bounded L&D interpretation",
            15,
            "400",
            "start",
            SOFT,
        ),
        box(45, 135, 205, 125, "1 • Enron hypergraph", ["148 nodes", "10,885 email events", "26,914 incidences"], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(290, 135, 205, 125, "2 • Project network", ["Deduplicate event members", "Undirected simple ties", "2,583 edges"], "#ecfeff", "#06b6d4", "#0e7490"),
        box(535, 135, 205, 125, "3 • Baseline access", ["Global efficiency", "0.5601", "Survivor-pair metric"], "#f0fdf4", "#22c55e", "#15803d"),
        box(780, 135, 205, 125, "4 • Rank once", ["Intact-network degree", "Static key-actor order"], "#f5f3ff", "#8b5cf6", "#6d28d9"),
        arrow(250, 198, 290, 198),
        arrow(495, 198, 535, 198),
        arrow(740, 198, 780, 198),
        box(780, 335, 205, 135, "5 • Targeted loss", ["Remove top k", "5 / 10 / 15 / 20 / 30", "Recompute efficiency"], "#fef2f2", "#ef4444", "#991b1b"),
        arrow(882, 260, 882, 335, TARGET),
        box(505, 335, 225, 135, "6 • Comparator", ["200 SHA-256-ranked draws", "Seed 20260925", "Mean + p05 / p95"], "#eff6ff", "#3b82f6", "#1d4ed8"),
        arrow(780, 402, 730, 402, RANDOM),
        box(230, 335, 225, 135, "7 • Compare resilience", ["Retained efficiency", "Gap growth", "Lower-tail diagnostic"], "#fff7ed", "#f59e0b", "#92400e"),
        arrow(505, 402, 455, 402, GOLD),
        box(230, 540, 755, 105, "8 • L&D interpretation", ["Diagnose structural continuity exposure before choosing succession, cross-training, mentoring, or documentation actions", "Do not infer tacit knowledge, employee value, learning effectiveness, or causal business impact"], "#f8fafc", "#94a3b8", "#334155"),
        arrow(342, 470, 342, 540, CYAN),
        arrow(618, 470, 618, 540, RANDOM),
        arrow(882, 470, 882, 540, TARGET),
        text(55, 700, "Key safeguard: the targeted rule is static degree loss, the comparator band is descriptive, and the network is a communication proxy rather than a knowledge measure.", 13, "700", "start", "#334155"),
        "</svg>",
    ]
    return "".join(output)


def architecture():
    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="650" viewBox="0 0 1200 650">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        text(55, 50, "From communication structure to knowledge-continuity questions", 30, "700"),
        text(55, 80, "The analysis separates what is observed, what is calculated, and what L&D may investigate next.", 15, "400", "start", SOFT),
        box(55, 125, 300, 125, "Observed evidence", ["Timestamped Enron email events", "Core address set", "No message content used"], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(450, 125, 300, 125, "Network evidence", ["Co-participation projection", "Shortest-path accessibility", "Sensitivity to actor removal"], "#f0fdf4", "#22c55e", "#15803d"),
        box(845, 125, 300, 125, "L&D questions", ["Where is access concentrated?", "Where is redundancy thin?", "Where should we investigate?"], "#fff7ed", "#f59e0b", "#92400e"),
        arrow(355, 188, 450, 188),
        arrow(750, 188, 845, 188),
        '<rect x="55" y="315" width="1090" height="240" rx="18" fill="#f8fafc" stroke="#cbd5e1"/>',
        text(85, 352, "Structural result", 17, "700"),
        text(85, 386, "Targeted loss", 13, "700", "start", TARGET),
        text(235, 386, "0.9735 → 0.8608 retained efficiency", 13, "600"),
        text(85, 420, "Comparator mean", 13, "700", "start", RANDOM),
        text(235, 420, "0.9978 → 0.9917", 13, "600"),
        text(85, 454, "Gap", 13, "700", "start", GOLD),
        text(235, 454, "0.0243 → 0.1309", 13, "600"),
        text(85, 505, "Interpretation boundary", 14, "700", "start", "#334155"),
        text(265, 505, "Communication topology can reveal structural exposure, not the content or uniqueness of employee knowledge.", 12.5, "600", "start", SOFT),
        text(55, 625, "Use the network to prioritize questions and resilience investigation, not to label people as irreplaceable.", 13, "700", "start", "#334155"),
        "</svg>",
    ]
    return "".join(output)


def evaluation():
    output = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="660" viewBox="0 0 1200 660">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        text(55, 50, "Evidence boundary and L&D interpretation", 30, "700"),
        box(55, 100, 1090, 96, "Observed network", ["148 nodes • 10,885 timestamped hyperedges • 2,583 projection edges • baseline efficiency 0.5601"], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(55, 220, 1090, 96, "Stress-test finding", ["Targeted retained efficiency falls 0.9735 → 0.8608 while the comparator mean remains close to baseline."], "#f0fdf4", "#22c55e", "#15803d"),
        box(55, 340, 1090, 96, "Comparator evidence", ["Targeted is below comparator p05 at every k; targeted-versus-comparator mean gap widens 0.0243 → 0.1309."], "#fff7ed", "#f59e0b", "#92400e"),
        box(55, 460, 1090, 96, "Claim boundary", ["Email connectivity is not tacit knowledge, expertise quality, employee value, learning effectiveness, or causal business performance."], "#fef2f2", "#ef4444", "#991b1b"),
        text(55, 630, "L&D use: identify where succession, cross-training, mentoring, documentation, or community-of-practice investigation may deserve attention.", 13, "700", "start", "#334155"),
        "</svg>",
    ]
    return "".join(output)


def render(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = read_curve()
    figures = {
        "research_design.svg": research_design(rows),
        "method.svg": method(),
        "architecture.svg": architecture(),
        "evaluation.svg": evaluation(),
    }

    for name, content in figures.items():
        ET.fromstring(content)
        (out_dir / name).write_text(content, encoding="utf-8")

    return figures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(ROOT / "assets"))
    args = parser.parse_args()
    figures = render(Path(args.out_dir))
    print("generated_figures:", len(figures))


if __name__ == "__main__":
    main()
