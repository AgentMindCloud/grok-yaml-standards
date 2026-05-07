#!/usr/bin/env python3
"""Generate 1200x630 OG-image posters for the GitHub Pages site.

Brand tokens come from .grok/brand-tokens.yaml. One poster per shareable
item (the root site + each grok-* standard). Output to docs/posters/.

Usage:
    python scripts/generate_posters.py
"""
from __future__ import annotations

import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path("docs/posters")
W, H = 1200, 630

# Brand tokens (mirrors .grok/brand-tokens.yaml)
BG = (13, 13, 13)            # #0D0D0D grok_black
SURFACE = (21, 32, 43)        # #15202B grok_surface
ACCENT = (29, 161, 242)       # #1DA1F2 grok_accent (X blue)
GOLD = (245, 197, 24)         # #F5C518 grok_gold
WHITE = (255, 255, 255)
MUTE = (136, 153, 166)        # #8899A6 grok_mute

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

# (slug, headline, subtitle)
ITEMS: list[tuple[str, str, str]] = [
    ("og-default",      "grok-yaml-standards",          "12 magic YAML standards for Grok on X"),
    ("grok-config",     "grok-config",                  "Repo-wide model settings & defaults"),
    ("grok-prompts",    "grok-prompts",                 "Reusable versioned prompt library"),
    ("grok-agent",      "grok-agent",                   "Persistent stateful Grok agents"),
    ("grok-workflow",   "grok-workflow",                "Multi-step automated processes"),
    ("grok-update",     "grok-update",                  "Smart repo & knowledge updates"),
    ("grok-test",       "grok-test",                    "AI-powered testing & validation"),
    ("grok-docs",       "grok-docs",                    "Auto-generated documentation"),
    ("grok-security",   "grok-security",                "Real-time security & compliance"),
    ("grok-tools",      "grok-tools",                   "Typed tool registry for agents & workflows"),
    ("grok-deploy",     "grok-deploy",                  "Deployment targets, env vars, health checks"),
    ("grok-analytics",  "grok-analytics",               "Opt-in telemetry with PII controls"),
    ("grok-ui",         "grok-ui",                      "Voice commands, dashboard widgets, shortcuts"),
    ("grok-swarm",      "grok-swarm",                   "Multi-agent orchestration patterns"),
    ("grok-voice",      "grok-voice",                   "Voice-first interface bindings"),
]


def render(slug: str, headline: str, subtitle: str, path: Path) -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Top accent stripe
    draw.rectangle((0, 0, W, 8), fill=ACCENT)
    # Bottom gold accent
    draw.rectangle((0, H - 4, W, H), fill=GOLD)

    # Side rule
    draw.rectangle((64, 110, 76, H - 110), fill=ACCENT)

    # Headline
    head_size = 96 if len(headline) <= 18 else 72
    head_font = ImageFont.truetype(FONT_BOLD, head_size)
    draw.text((110, 180), headline, font=head_font, fill=WHITE)

    # Subtitle
    sub_font = ImageFont.truetype(FONT_REGULAR, 36)
    draw.text((110, 320), subtitle, font=sub_font, fill=MUTE)

    # Footer mark
    mark_font = ImageFont.truetype(FONT_MONO, 24)
    draw.text((110, H - 90), "agentmindcloud.github.io/grok-yaml-standards", font=mark_font, fill=ACCENT)

    # Gold dot (mirrors logo)
    cx, cy, r = W - 130, 200, 28
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD)

    img.save(path, "PNG", optimize=True)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, headline, subtitle in ITEMS:
        out = OUT_DIR / f"{slug}.png"
        render(slug, headline, subtitle, out)
        print(f"  wrote {out}")


if __name__ == "__main__":
    main()
