function toggleMenu() { document.getElementById('mobileMenu').classList.toggle('open') }
function closeMenu() { document.getElementById('mobileMenu').classList.remove('open') }
document.addEventListener('click', function (e) { if (!document.querySelector('.nav-outer').contains(e.target)) closeMenu() });

// Word stagger reveal on hero h1
(function () {
  var h1 = document.querySelector('.hero h1');
  if (!h1) return;
  var html = h1.innerHTML;
  var words = html.split(' ');
  h1.innerHTML = words.map(function (w, i) {
    return '<span class="word" style="animation-delay:' + (i * 0.08) + 's">' + w + '</span>';
  }).join(' ');
})();

// CountUp animation
window.initCountUp = function (elements) {
  if (!elements || !elements.length) return;
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) return;
      var el = entry.target;
      var targetStr = el.getAttribute('data-target');
      var isFloat = targetStr.indexOf('.') !== -1;
      var target = isFloat ? parseFloat(targetStr) : parseInt(targetStr);
      var duration = 1800;
      var start = null;
      function step(ts) {
        if (!start) start = ts;
        var progress = Math.min((ts - start) / duration, 1);
        var ease = 1 - Math.pow(1 - progress, 3);
        var val = ease * target;
        el.textContent = isFloat ? val.toFixed(1) : Math.floor(val);
        if (progress < 1) requestAnimationFrame(step);
        else el.textContent = targetStr;
      }
      requestAnimationFrame(step);
      observer.unobserve(el);
    });
  }, { threshold: 0.5 });
  elements.forEach(function (c) { observer.observe(c); });
};
window.initCountUp(document.querySelectorAll('.countup'));

// Scroll Progress Indicator
(function () {
  const scrollProgress = document.getElementById('scroll-progress');
  if (scrollProgress) {
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      scrollProgress.style.width = scrolled + '%';
    });
  }
})();

// SaaS Scroll Reveal & Graphs Animation
(function () {
  var revealElements = document.querySelectorAll('.reveal, .hdw-bar-fill, .mini-chart-fill');
  var observer = new IntersectionObserver(function (entries, currentObserver) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        var el = entry.target;
        if (el.classList.contains('reveal')) {
          el.classList.add('active');
        }
        if (el.hasAttribute('data-height')) {
          el.style.height = el.getAttribute('data-height');
        }
        if (el.hasAttribute('data-width')) {
          el.style.width = el.getAttribute('data-width');
        }
        currentObserver.unobserve(el);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });
  revealElements.forEach(function (el) {
    observer.observe(el);
  });
  // Quick trigger for the hero float widget since it loads immediately
  setTimeout(() => {
    var widget = document.getElementById('hero-widget');
    if (widget) {
      widget.classList.add('active');
      widget.querySelectorAll('.hdw-bar-fill').forEach(el => {
        el.style.height = el.getAttribute('data-height');
      });
    }
  }, 100);
})();

// Advanced SaaS Interactions: Spotlight, Magnetic Buttons, ROI Calculator
(function () {
  const spotlight = document.getElementById('cursor-spotlight');
  const grid = document.getElementById('interactive-grid');

  document.addEventListener('mousemove', (e) => {
    if (spotlight) {
      spotlight.style.left = e.clientX + 'px';
      spotlight.style.top = e.clientY + 'px';
    }
    if (grid) {
      if (!grid.classList.contains('active')) grid.classList.add('active');
      grid.style.setProperty('--mouse-x', e.clientX + 'px');
      grid.style.setProperty('--mouse-y', e.clientY + 'px');
    }
  });
  document.addEventListener('mouseleave', () => {
    if (grid) grid.classList.remove('active');
  });

  const magneticTargets = document.querySelectorAll('.btn, .nav-links a, .nav-cta, .tab-btn');
  magneticTargets.forEach(target => {
    target.addEventListener('mousemove', (e) => {
      const rect = target.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const deltaX = (x - centerX) / centerX;
      const deltaY = (y - centerY) / centerY;
      target.classList.add('magnetic');
      target.classList.remove('reset');
      target.style.transform = `translate3d(${deltaX * 8}px, ${deltaY * 8}px, 0)`;
    });
    target.addEventListener('mouseleave', () => {
      target.classList.remove('magnetic');
      target.style.transform = '';
      target.classList.add('reset');
      setTimeout(() => target.classList.remove('reset'), 400);
    });
  });

  const slider = document.getElementById('rev-slider');
  const revVal = document.getElementById('rev-val');
  const leakVal = document.getElementById('leak-val');
  const leakEquiv = document.getElementById('leak-equiv');
  if (slider && revVal && leakVal) {
    const updateROI = () => {
      const val = parseInt(slider.value);
      revVal.textContent = val;
      const leakMillions = val * 0.2 * 12;

      let leakStr = '';
      if (window.isForeign) {
        const leakUsd = val * 10000 * 0.2 * 12;
        if (leakUsd >= 1000000) {
          leakStr = '$' + (leakUsd / 1000000).toFixed(1).replace('.0', '') + 'M';
        } else {
          leakStr = '$' + (leakUsd / 1000).toFixed(0) + 'K';
        }
        leakVal.textContent = leakStr;
        // Equivalence for foreign
        const salaries = Math.round(leakUsd / 40000);
        if (leakEquiv) leakEquiv.textContent = "That's roughly " + salaries + " senior employee " + (salaries === 1 ? 'salary' : 'salaries') + " \u2014 lost silently every year.";
      } else {
        if (leakMillions >= 10) {
          leakStr = (leakMillions / 10).toFixed(1).replace('.0', '') + ' Crore';
        } else {
          leakStr = (leakMillions * 10).toFixed(0) + ' Lakh';
        }
        leakVal.textContent = 'PKR ' + leakStr;
        // Equivalence for PKR (avg senior salary ~4 Lakh/mo = 48 Lakh/yr)
        const salaries = Math.round((leakMillions * 10) / 48);
        if (leakEquiv && salaries > 0) leakEquiv.textContent = "That's roughly " + salaries + " senior employee " + (salaries === 1 ? 'salary' : 'salaries') + " \u2014 lost silently every year.";
      }

      const pct = ((val - slider.min) / (slider.max - slider.min)) * 100;
      slider.style.background = `linear-gradient(to right, var(--orange) ${pct}%, rgba(255,255,255,0.08) ${pct}%)`;
    };
    window.updateROI = updateROI;
    slider.addEventListener('input', updateROI);
    updateROI();
  }
})();

// Dynamic Cursor-Tracking Card Glow
document.querySelectorAll('.cs-card').forEach(card => {
  card.addEventListener('mousemove', e => {
    const rect = card.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    card.style.setProperty('--x', x + '%');
    card.style.setProperty('--y', y + '%');
  });
  card.addEventListener('mouseleave', () => {
    card.style.removeProperty('--x');
    card.style.removeProperty('--y');
  });
});

// SVG Micro-Animations Hover Trigger
document.querySelectorAll('.hover-target').forEach(target => {
  target.addEventListener('mouseenter', () => {
    const drawEls = target.querySelectorAll('.anim-draw, .anim-draw-fill');
    drawEls.forEach(el => {
      el.style.animation = 'none';
      el.offsetHeight; /* trigger reflow */
      el.style.animation = null;
    });
  });
});

// Parallax Background Elements
(function () {
  const parallaxElements = document.querySelectorAll('.parallax-layer');
  let ticking = false;

  function updateParallax() {
    parallaxElements.forEach(el => {
      const speed = parseFloat(el.getAttribute('data-speed')) || 0;
      const rect = el.parentElement.getBoundingClientRect();
      const yPos = (window.innerHeight - rect.top) * speed * 0.5;
      el.style.transform = `translate3d(0, ${yPos}px, 0)`;
    });
    ticking = false;
  }

  window.addEventListener('scroll', () => {
    if (!ticking && parallaxElements.length > 0) {
      window.requestAnimationFrame(updateParallax);
      ticking = true;
    }
  }, { passive: true });
})();

function applyForeignFormatting() {
    document.querySelectorAll('.geo-cur').forEach(el => {
        if (el.dataset.usd) el.innerHTML = el.dataset.usd;
    });

    document.querySelectorAll('.geo-cur-stat').forEach(el => {
        if (el.dataset.target) {
        el.innerHTML = el.dataset.prefix + ' <span class="countup" data-target="' + el.dataset.target + '">0</span> ' + (el.dataset.suffix || '');
        }
    });
    window.isForeign = true;
    if (window.initCountUp) {
        window.initCountUp(document.querySelectorAll('.geo-cur-stat .countup'));
    }

    const rp = document.getElementById('rev-prefix');
    if (rp) rp.innerText = '$';
    const rs = document.getElementById('rev-suffix');
    if (rs) rs.innerText = 'K';

    if (typeof window.updateROI === 'function') {
        window.updateROI();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const cachedGeo = localStorage.getItem('closimoGeoData');
    if(cachedGeo && cachedGeo !== 'PK') {
        applyForeignFormatting();
    } else if(!cachedGeo) {
        fetch('https://get.geojs.io/v1/ip/country.json')
        .then(res => res.json())
        .then(data => {
            localStorage.setItem('closimoGeoData', data.country);
            if (data.country !== 'PK') {
                applyForeignFormatting();
            }
        })
        .catch(err => console.log('GeoIP failed, defaulting to PKR.'));
    }

    fetch('data.json')
    .then(response => response.json())
    .then(testimonials => {
        function renderStars() {
            return '<div class="testi-stars" style="color:#FFB800; display:flex; gap:3px;">' + Array(5).fill('<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z" fill="currentColor"/></svg>').join('') + '</div>';
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
        const trackLtr = document.getElementById('track-ltr');
        const trackRtl = document.getElementById('track-rtl');
        if (trackLtr) trackLtr.innerHTML = trackItems;
        if (trackRtl) trackRtl.innerHTML = trackItems;

        if (window.isForeign) {
            document.querySelectorAll('.geo-cur').forEach(el => {
                if (el.dataset.usd) el.innerHTML = el.dataset.usd;
            });
        }
    })
    .catch(error => console.error("Could not fetch testimonials", error));
});

document.addEventListener('DOMContentLoaded', () => {
  const overlay = document.querySelector('.page-transition-overlay');
  if (overlay) {
    setTimeout(() => overlay.classList.add('is-loaded'), 50);
  }
  document.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', function (e) {
      const target = this.getAttribute('target');
      const href = this.getAttribute('href');
      if (target === '_blank' || !href || href.startsWith('#') || href.startsWith('tel:') || href.startsWith('mailto:')) return;
      if (this.hostname !== window.location.hostname && href.indexOf('http') !== -1) return;
      e.preventDefault();
      if (overlay) overlay.classList.remove('is-loaded');
      setTimeout(() => {
        window.location.href = href;
      }, 400);
    });
  });
});
window.addEventListener('pageshow', (event) => {
  const overlay = document.querySelector('.page-transition-overlay');
  if (event.persisted && overlay) {
    overlay.classList.add('is-loaded');
  }
});

// Back to Top functionality
document.addEventListener('DOMContentLoaded', () => {
  const bttBtn = document.getElementById('back-to-top');
  if (bttBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 600) {
        bttBtn.classList.add('visible');
      } else {
        bttBtn.classList.remove('visible');
      }
    }, { passive: true });

    bttBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});


// Before/After staggered slide-in animation
(function () {
  const baWrap = document.querySelector('.ba-wrap');
  if (!baWrap) return;
  const baItems = baWrap.querySelectorAll('.ba-item');
  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        baItems.forEach(function (item, i) {
          setTimeout(function () {
            item.classList.add('ba-visible');
          }, i * 100);
        });
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  observer.observe(baWrap);
})();
