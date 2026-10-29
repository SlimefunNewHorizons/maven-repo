#!/usr/bin/env python3
"""Regenera la lista de artefactos de index.html (entre marcadores) recorriendo el repo.
Uso: python3 scripts/generar_indice.py"""
import html, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
base = root / "com/github/drakescraft_labs"
rows = {"t2": [], "prod": [], "otras": []}
for art in sorted(base.iterdir(), key=lambda p: p.name.lower()):
    if not art.is_dir():
        continue
    for ver in sorted(p for p in art.iterdir() if p.is_dir()):
        v = ver.name
        if "26.x" in v:
            k = "t2"
        elif "1.21.11" in v or v.endswith("DRAKE-v11-SNAPSHOT") or v.endswith("-DRAKE-SNAPSHOT"):
            k = "prod"
        else:
            k = "otras"
        rows[k].append((art.name, v))
titles = {"t2": "T2 &middot; Minecraft 26.2 &middot; Java 25", "prod": "Produccion &middot; Minecraft 1.21.11 &middot; Java 21", "otras": "Otras versiones / legado"}
out = []
for k in ("prod", "t2", "otras"):
    if not rows[k]:
        continue
    out.append(f'<h3>{titles[k]} <span class="muted">({len(rows[k])})</span></h3><div class="grid">')
    for a, v in rows[k]:
        e = html.escape
        out.append(f'<article class="artifact"><strong>{e(a)}</strong><small>{e(v)}</small>'
                   f'<p></p><a href="com/github/drakescraft_labs/{e(a)}/{e(v)}/">Abrir carpeta</a></article>')
    out.append('</div>')
block = "\n".join(out)
p = root / "index.html"
s = p.read_text(encoding="utf-8")
s = re.sub(r"(<!--ARTIFACTS:START-->).*?(<!--ARTIFACTS:END-->)", lambda m: m.group(1) + "\n" + block + "\n" + m.group(2), s, flags=re.S)
p.write_text(s, encoding="utf-8")
print({k: len(v) for k, v in rows.items()})
