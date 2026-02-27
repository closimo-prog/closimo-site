import re

with open('code.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add symbol definition right after <body>
star_symbol = """
  <svg style="display: none;">
    <symbol id="icon-star" viewBox="0 0 24 24">
      <path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
    </symbol>
  </svg>
"""

if 'id="icon-star"' not in html:
    html = html.replace('<body>', '<body>\n' + star_symbol)

# 2. Replace the massive star SVGs
star_svg_pattern = re.compile(r'<svg viewBox="0 0 24 24">\s*<path\s*d="M12 2l3\.09 6\.26L22 9\.27l-5 4\.87 1\.18 6\.88L12 17\.77l-6\.18 3\.25L7 14\.14 2 9\.27l6\.91-1\.01L12 2z"\s*/>\s*</svg>', re.IGNORECASE)

html = star_svg_pattern.sub('<svg viewBox="0 0 24 24"><use href="#icon-star"></use></svg>', html)

# 3. Strip leading whitespace from all lines to flatten it out (since formatters explode nested tags)
# We will just do a simple replacement of \n + multiple spaces into a single \n
# Or even safer, remove blank lines.
lines = [line.strip() for line in html.split('\n') if line.strip() != '']
html = '\n'.join(lines)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Compressed SVGs and stripped whitespace. Lines reduced to:", len(lines))
