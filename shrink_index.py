import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

testimonials_html = """
    <div class="testi-marquee-wrap">
      <div class="testi-track ltr" id="track-ltr"></div>
    </div>
    <div class="testi-marquee-wrap">
      <div class="testi-track rtl" id="track-rtl"></div>
    </div>
"""

pattern_testi_cut = re.compile(r'<div class="testi-marquee-wrap">.*?</div>\s*</div>\s*</section>', re.DOTALL)
if pattern_testi_cut.search(html):
    html = pattern_testi_cut.sub(testimonials_html + '\n  </section>', html)

    script = """
  <script>
    const testimonials = [
      {
        text: "400 leads a month and barely 1–2 closing. That's not a lead problem, that's a process problem. CLOSIMO found PKR 48 Lakh in annual leakage across 3 root causes. The roadmap gave us a clear path to 5–7x more deals with the same spend.",
        name: "Ahsan Riaz",
        role: "Managing Director · Insignia Business Solutions"
      },
      {
        text: "We had the product and the market. What we were missing was a repeatable way to close. CLOSIMO found exactly where deals were dying and gave us the system to fix it. PKR 2.2 Crore closed in the first 90 days.",
        name: "Riaz Murad",
        role: "Founder · Smart Light Arabia"
      },
      {
        text: "I knew something was off but couldn't put a number on it. CLOSIMO put a number on it, then helped us fix it. Profitability doubled within the year.",
        name: "Ahmed El Basel",
        role: "Managing Partner · Al Deyaa Media · Etisalat Partner"
      },
      {
        text: "PKR 3.7 Crore closed in 90 days. 50x return on the engagement. I've invested in a lot of things. This was the fastest return I've ever seen.",
        name: "Murad Saleem",
        role: "CEO · Harvest Solar"
      },
      {
        text: "The team was working hard but deals weren't closing at the rate they should. CLOSIMO showed us exactly where the process was breaking down. We went from chasing proposals to a system that runs itself.",
        name: "Hashmat Abbas",
        role: "Head of Business · Proline UK"
      },
      {
        text: "Twenty years building this business. I thought I knew where the problems were. CLOSIMO showed me I was looking in the wrong place entirely. We finally have a pipeline we can predict.",
        name: "Ghulam Mujtaba",
        role: "Founder · Maxtech Corporation"
      },
      {
        text: "30% jump in revenue in the same market, with the same team. The only thing that changed was the process. CLOSIMO found what was broken and built the fix into the operation.",
        name: "Adeeb Ahmed",
        role: "Managing Partner · ARC LTD"
      },
      {
        text: "What I valued most was the honesty. They told us what was actually wrong, not what we wanted to hear. That kind of transparency is rare and it's what made the whole engagement worth it.",
        name: "Vasil Dimov",
        role: "Managing Director · Vasdan & Co"
      },
      {
        text: "Healthcare is process-heavy by nature. What CLOSIMO found was that our sales process had no process at all. They fixed that. Profits doubled within the same year.",
        name: "Waleed Mushfiq",
        role: "CEO · 3W Healthcare"
      },
      {
        text: "Security is a relationship business. We were winning on relationships and losing on process. CLOSIMO fixed the process without touching what made us good at the relationship side.",
        name: "Faizan Hamus",
        role: "CEO · Al Taaraf Security Group"
      },
      {
        text: "We were losing clients we couldn't afford to lose and didn't know why. The audit went three layers deep and found exactly where. The numbers they put on it made the decision to fix it an easy one.",
        name: "Wasiq Ali Khan",
        role: "Managing Partner · Al Makkah Group"
      }
    ];

    function renderStars() {
      return '<div class="testi-stars">' + Array(5).fill('<svg viewBox="0 0 24 24"><use href="#icon-star"></use></svg>').join('') + '</div>';
    }

    function createCard(t) {
      return `
        <div class="testi-card">
          ${renderStars()}
          <div class="testi-text">${t.text}</div>
          <div class="testi-author">
            <div>
              <div class="testi-name">${t.name}</div>
              <div class="testi-role">${t.role}</div>
            </div>
          </div>
        </div>
      `;
    }

    const trackItems = [...testimonials, ...testimonials].map(createCard).join('');
    document.getElementById('track-ltr').innerHTML = trackItems;
    document.getElementById('track-rtl').innerHTML = trackItems;
  </script>
</body>
"""
    html = html.replace('</body>', script)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Testimonials replaced")
else:
    print("Testimonials not replaced")
