import re
import base64

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract CSS
style_match = re.search(r'<style>(.*?)</style>', content, flags=re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    content = content[:style_match.start()] + '<link rel="stylesheet" href="style.css">' + content[style_match.end():]

# 2. Extract Base64 Images
img_matches = list(re.finditer(r'src="(data:image/(\w+);base64,([^"]+))"', content))
count = 1
for match in img_matches:
    full_str = match.group(1)
    if full_str not in content:
        continue # already replaced
    ext = match.group(2)
    b64_data = match.group(3)
    try:
        data_bytes = base64.b64decode(b64_data)
        img_filename = f'image{count}.{ext}'
        with open(img_filename, 'wb') as img_f:
            img_f.write(data_bytes)
        content = content.replace(full_str, img_filename)
        count += 1
    except Exception as e:
        print(f"Error decoding image {count}: {e}")

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Extracted CSS and {count-1} images. New HTML size: {len(content)} bytes.")
