import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace static currencies with span wrappers

# HERO
html = html.replace('PKR 10M–100M', '<span class="geo-cur" data-usd="$35K–$350K">PKR 10M–100M</span>')
html = html.replace('PKR 4 Crore', '<span class="geo-cur" data-usd="$140,000+">PKR 4 Crore</span>')

# STATS BAR
html = html.replace('<em>PKR <span class="countup" data-target="120">0</span></em> Crore', '<em><span class="geo-cur-stat" data-prefix="$" data-target="4.4" data-suffix="M+">PKR <span class="countup" data-target="120">0</span> Crore</span></em>')
html = html.replace('<em>PKR 7</em> Crore+', '<em><span class="geo-cur" data-usd="$250K+">PKR 7 Crore+</span></em>')

# AUDIT CARDS
html = html.replace('13M PKR', '<span class="geo-cur" data-usd="$45K">13M PKR</span>')
html = html.replace('PKR 4.0 Crore', '<span class="geo-cur" data-usd="$140,000+">PKR 4.0 Crore</span>')
html = html.replace('PKR 2.7 Crore', '<span class="geo-cur" data-usd="$95,000+">PKR 2.7 Crore</span>')
html = html.replace('PKR 48 Lakh', '<span class="geo-cur" data-usd="$17,000+">PKR 48 Lakh</span>')

# CASE STUDIES
html = html.replace('PKR 120 Crore Generated', '<span class="geo-cur" data-usd="$4.4M+ Generated">PKR 120 Crore Generated</span>')
html = html.replace('PKR 75 Crore', '<span class="geo-cur" data-usd="$2.6M+">PKR 75 Crore</span>')
html = html.replace('PKR 28 Crore', '<span class="geo-cur" data-usd="$1M+">PKR 28 Crore</span>')
html = html.replace('PKR 22 Crore', '<span class="geo-cur" data-usd="$780,000+">PKR 22 Crore</span>')
html = html.replace('PKR 75 Lakh', '<span class="geo-cur" data-usd="$26,000+">PKR 75 Lakh</span>')
html = html.replace('PKR 7 Lakh', '<span class="geo-cur" data-usd="$2,500+">PKR 7 Lakh</span>')

# FAQ
html = html.replace('PKR 2.5 Lakh', '<span class="geo-cur" data-usd="$900">PKR 2.5 Lakh</span>')
html = html.replace('PKR 1M', '<span class="geo-cur" data-usd="$3,500">PKR 1M</span>')

# FINAL CTA & TOPBAR
html = html.replace('PKR 7 Crore+', '<span class="geo-cur" data-usd="$250,000+">PKR 7 Crore+</span>')
html = html.replace('PKR 120 CRORE', '<span class="geo-cur" data-usd="$4.4M+">PKR 120 CRORE</span>')

# Ensure the slider has a base logic swap
# It was: <div class="roi-revenue-display">PKR <span id="rev-val">10</span> Million</div>
# It was: <div class="roi-result-value" id="leak-val">PKR 2.4 Crore</div>
html = html.replace('<div class="roi-revenue-display">PKR <span id="rev-val">10</span> Million</div>', '<div class="roi-revenue-display"><span id="rev-prefix">PKR </span><span id="rev-val">10</span> <span id="rev-suffix"> Million</span></div>')

# Append Geo-IP Script just before </body>
geo_script = """
  <script>
    document.addEventListener('DOMContentLoaded', () => {
      fetch('https://get.geojs.io/v1/ip/country.json')
        .then(res => res.json())
        .then(data => {
          if (data.country !== 'PK') {
             document.querySelectorAll('.geo-cur').forEach(el => {
               if(el.dataset.usd) el.innerHTML = el.dataset.usd;
             });
             
             document.querySelectorAll('.geo-cur-stat').forEach(el => {
               if(el.dataset.target) {
                  el.innerHTML = el.dataset.prefix + ' <span class="countup" data-target="' + el.dataset.target + '">0</span> ' + (el.dataset.suffix || '');
               }
             });
             window.isForeign = true;
             
             // Update ROI calculator labels immediately if logic exists
             const rp = document.getElementById('rev-prefix');
             if(rp) rp.innerText = '$';
             const rs = document.getElementById('rev-suffix');
             if(rs) rs.innerText = 'K';
             
             if(typeof window.updateROI === 'function') {
                window.updateROI(); // re-trigger calc if exists
             }
          }
        })
        .catch(err => console.log('GeoIP failed, defaulting to PKR.'));
    });
  </script>
"""

# Testimonials array text needs manual swap via replace since it's JS (optional, but good)
html = html.replace('PKR 48 Lakh', '<span class="geo-cur" data-usd="$17,000+">PKR 48 Lakh</span>')
html = html.replace('PKR 2.2 Crore', '<span class="geo-cur" data-usd="$78,000+">PKR 2.2 Crore</span>')
html = html.replace('PKR 3.7 Crore', '<span class="geo-cur" data-usd="$130,000+">PKR 3.7 Crore</span>')

if 'GeoIP failed' not in html:
    html = html.replace('</body>', geo_script + '\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Replaced exact PKR strings.')
