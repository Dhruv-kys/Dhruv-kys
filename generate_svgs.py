"""
Generates all SVG image assets for Dhruv Diwakirti's GitHub profile README.
Run this script to regenerate images/ folder contents.
"""

import os

OUT = "images"
os.makedirs(OUT, exist_ok=True)

GREEN   = "#00ff88"
ORANGE  = "#ff6b35"
BG      = "#0d1117"
DIM     = "#30363d"
GRAY    = "#8b949e"
WHITE   = "#e6edf3"
MONO    = "'Courier New', Courier, monospace"

# ─── 1. BANNER ────────────────────────────────────────────────────────────────

banner = f"""<svg width="900" height="190" viewBox="0 0 900 190" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
      <path d="M 30 0 L 0 0 0 30" fill="none" stroke="{GREEN}" stroke-width="0.3" opacity="0.15"/>
    </pattern>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{GREEN}" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="{BG}" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- bg -->
  <rect width="900" height="190" fill="{BG}"/>
  <rect width="900" height="190" fill="url(#grid)"/>

  <!-- left gradient accent -->
  <rect width="340" height="190" fill="url(#fade)"/>

  <!-- left border bar -->
  <rect x="0" y="0" width="4" height="190" fill="{GREEN}"/>

  <!-- top / bottom hairlines -->
  <line x1="4" y1="0" x2="900" y2="0" stroke="{DIM}" stroke-width="1"/>
  <line x1="4" y1="189" x2="900" y2="189" stroke="{DIM}" stroke-width="1"/>

  <!-- prompt line -->
  <text x="26" y="60" font-family="{MONO}" font-size="14" fill="{GRAY}">~/dhruv-kys $ <tspan fill="{GREEN}">whoami</tspan></text>

  <!-- name -->
  <text x="26" y="120" font-family="{MONO}" font-weight="bold" font-size="54" fill="{GREEN}" letter-spacing="-1">DHRUV DIWAKIRTI</text>

  <!-- tagline -->
  <text x="28" y="152" font-family="{MONO}" font-size="15" fill="{GRAY}">software engineer  ·  ai systems  ·  llm pipelines  ·  backend infra</text>

  <!-- cursor -->
  <rect x="28" y="162" width="11" height="18" fill="{GREEN}" opacity="0.9">
    <animate attributeName="opacity" values="0.9;0;0.9" dur="1.2s" repeatCount="indefinite"/>
  </rect>

  <!-- corner tag -->
  <text x="870" y="175" font-family="{MONO}" font-size="11" fill="{DIM}" text-anchor="end">JSS NOIDA '27</text>
</svg>"""

# ─── 2. SOCIAL BUTTONS ────────────────────────────────────────────────────────

def social_svg(label, icon_char, accent=GREEN):
    return f"""<svg width="190" height="44" viewBox="0 0 190 44" xmlns="http://www.w3.org/2000/svg">
  <rect width="190" height="44" rx="6" fill="{BG}"/>
  <rect x="0.5" y="0.5" width="189" height="43" rx="5.5" fill="none" stroke="{DIM}"/>
  <rect x="0" y="0" width="4" height="44" rx="3" fill="{accent}"/>
  <text x="20" y="28" font-family="{MONO}" font-size="13" fill="{accent}">{icon_char}</text>
  <text x="38" y="28" font-family="{MONO}" font-size="13" fill="{WHITE}">{label}</text>
</svg>"""

# ─── 3. ABOUT / STATS CARD ────────────────────────────────────────────────────

def make_bar(pct, color=GREEN, width=160):
    filled = int(width * pct)
    empty  = width - filled
    chars_f = int(filled  / (width / 20))
    chars_e = 20 - chars_f
    return "█" * chars_f + "░" * chars_e

about = f"""<svg width="900" height="310" viewBox="0 0 900 310" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="0.8" fill="{GREEN}" opacity="0.12"/>
    </pattern>
  </defs>

  <!-- bg -->
  <rect width="900" height="310" rx="8" fill="{BG}"/>
  <rect width="900" height="310" rx="8" fill="url(#dots)"/>
  <rect x="0.5" y="0.5" width="899" height="309" rx="7.5" fill="none" stroke="{DIM}"/>

  <!-- left accent bar -->
  <rect x="0" y="0" width="4" height="310" rx="3" fill="{GREEN}"/>

  <!-- title row -->
  <text x="22" y="36" font-family="{MONO}" font-size="13" fill="{GRAY}">  ┌─ profile.json ──────────────────────────────────────────────────────────────</text>

  <!-- row data -->
  <!-- col 1 labels -->
  <text x="22" y="68"  font-family="{MONO}" font-size="13" fill="{GRAY}">  │  <tspan fill="{GREEN}">role</tspan>       </text>
  <text x="22" y="92"  font-family="{MONO}" font-size="13" fill="{GRAY}">  │  <tspan fill="{GREEN}">college</tspan>    </text>
  <text x="22" y="116" font-family="{MONO}" font-size="13" fill="{GRAY}">  │  <tspan fill="{GREEN}">company</tspan>    </text>
  <text x="22" y="140" font-family="{MONO}" font-size="13" fill="{GRAY}">  │  <tspan fill="{GREEN}">focus</tspan>      </text>
  <text x="22" y="164" font-family="{MONO}" font-size="13" fill="{GRAY}">  │  <tspan fill="{GREEN}">shipped</tspan>    </text>
  <text x="22" y="188" font-family="{MONO}" font-size="13" fill="{GRAY}">  │  <tspan fill="{GREEN}">stack</tspan>      </text>
  <text x="22" y="212" font-family="{MONO}" font-size="13" fill="{GRAY}">  │  <tspan fill="{GREEN}">status</tspan>     </text>

  <!-- col 1 values -->
  <text x="150" y="68"  font-family="{MONO}" font-size="13" fill="{WHITE}">SWE Intern @ Cubical Frames</text>
  <text x="150" y="92"  font-family="{MONO}" font-size="13" fill="{WHITE}">JSS Academy of Technical Education, Noida</text>
  <text x="150" y="116" font-family="{MONO}" font-size="13" fill="{WHITE}">Cubical Frames</text>
  <text x="150" y="140" font-family="{MONO}" font-size="13" fill="{WHITE}">AI Systems  ·  LLM Pipelines  ·  Backend</text>
  <text x="150" y="164" font-family="{MONO}" font-size="13" fill="{WHITE}">HireSense AI  ·  ExpenseMCP  ·  ASR Router</text>
  <text x="150" y="188" font-family="{MONO}" font-size="13" fill="{WHITE}">FastAPI  ·  LangChain  ·  Docker  ·  AWS  ·  GCP</text>
  <text x="150" y="212" font-family="{MONO}" font-size="13" fill="{GREEN}">[ ████████████░░ ]  shipping</text>

  <!-- divider -->
  <line x1="22" y1="228" x2="878" y2="228" stroke="{DIM}" stroke-width="0.8"/>

  <!-- language bars -->
  <text x="22" y="250" font-family="{MONO}" font-size="12" fill="{GRAY}">  │  Languages</text>

  <text x="150" y="250" font-family="{MONO}" font-size="12" fill="{GREEN}">Python</text>
  <text x="215" y="250" font-family="{MONO}" font-size="12" fill="{DIM}">████████████████░░░░</text>
  <text x="430" y="250" font-family="{MONO}" font-size="12" fill="{GRAY}">80%</text>

  <text x="150" y="270" font-family="{MONO}" font-size="12" fill="{ORANGE}">Bash  </text>
  <text x="215" y="270" font-family="{MONO}" font-size="12" fill="{DIM}">███░░░░░░░░░░░░░░░░░</text>
  <text x="430" y="270" font-family="{MONO}" font-size="12" fill="{GRAY}">14%</text>

  <text x="150" y="290" font-family="{MONO}" font-size="12" fill="{GRAY}">Other </text>
  <text x="215" y="290" font-family="{MONO}" font-size="12" fill="{DIM}">█░░░░░░░░░░░░░░░░░░░</text>
  <text x="430" y="290" font-family="{MONO}" font-size="12" fill="{GRAY}"> 6%</text>

  <!-- close line -->
  <text x="22" y="308" font-family="{MONO}" font-size="13" fill="{GRAY}">  └──────────────────────────────────────────────────────────────────────────────</text>
</svg>"""

# ─── 4. FOOTER ────────────────────────────────────────────────────────────────

footer = f"""<svg width="900" height="80" viewBox="0 0 900 80" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="80" fill="{BG}"/>
  <line x1="0" y1="0" x2="900" y2="0" stroke="{DIM}" stroke-width="1"/>

  <!-- left accent -->
  <rect x="0" y="0" width="4" height="80" fill="{GREEN}"/>

  <text x="26" y="34" font-family="{MONO}" font-size="13" fill="{GRAY}">~/dhruv-kys $ <tspan fill="{GREEN}">echo</tspan> <tspan fill="{WHITE}">"shipped &gt; perfect"</tspan></text>
  <text x="26" y="58" font-family="{MONO}" font-size="13" fill="{GRAY}">shipped &gt; perfect</text>

  <!-- cursor -->
  <rect x="26" y="64" width="9" height="13" fill="{GREEN}" opacity="0.9">
    <animate attributeName="opacity" values="0.9;0;0.9" dur="1.2s" repeatCount="indefinite"/>
  </rect>

  <!-- right tag -->
  <text x="874" y="46" font-family="{MONO}" font-size="12" fill="{DIM}" text-anchor="end">if this helped → ⭐</text>
</svg>"""

# ─── WRITE ALL FILES ──────────────────────────────────────────────────────────

files = {
    f"{OUT}/banner.svg":   banner,
    f"{OUT}/about.svg":    about,
    f"{OUT}/footer.svg":   footer,
    f"{OUT}/linkedin.svg": social_svg("LinkedIn",  "in", GREEN),
    f"{OUT}/gmail.svg":    social_svg("loltreat1@gmail.com", "@", "#EA4335"),
    f"{OUT}/github.svg":   social_svg("Dhruv-kys", "gh", GRAY),
}

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)
    print(f"  ✓  {path}")

print("\nAll SVGs generated.")
