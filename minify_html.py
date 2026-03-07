import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove HTML comments except some standard ones if any (none needed here)
html = re.sub(r'<!--(.*?)-->', '', html, flags=re.DOTALL)

# Find all SVGs and compress them to a single line
def compress_svg(match):
    # remove newlines and extra spaces within SVG tags
    svg = match.group(0)
    svg = re.sub(r'\s+', ' ', svg)
    svg = svg.replace('> <', '><')
    return svg

html = re.sub(r'<svg.*?</svg>', compress_svg, html, flags=re.DOTALL)

# Also remove extra empty lines
html = re.sub(r'\n\s*\n', '\n', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Optimized HTML length')
