/* CLOSIMO booking. Every [data-book] button opens the Tally form "Find Where Your Deals Go".
   Hidden fields sent to Tally: offer (diagnosis | audit), tier (3-5 | 6-10 | 10+), page. */
(function () {
  var FORM = '2jaP6V';
  var path = location.pathname.replace(/\/index\.html$/, '/');
  var page = /\/findings\/$/.test(path) ? 'findings' : /\/about\/$/.test(path) ? 'about' : 'home';
  function tier() {
    var b = document.querySelector('.seg button[aria-checked="true"]');
    if (!b) return '';
    var t = b.textContent;
    return /6 to 10/.test(t) ? '6-10' : /More than 10/.test(t) ? '10+' : '3-5';
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-book]');
    if (!a) return;
    e.preventDefault();
    var offer = a.getAttribute('data-book') === 'audit' ? 'audit' : 'diagnosis';
    var hidden = { offer: offer, tier: offer === 'audit' ? tier() : '', page: page };
    if (window.gtag) gtag('event', 'book_click', { offer: offer, page: page });
    if (window.Tally && Tally.openPopup) {
      Tally.openPopup(FORM, { layout: 'modal', width: 560, overlay: true, hiddenFields: hidden });
    } else {
      var q = Object.keys(hidden).filter(function (k) { return hidden[k]; })
        .map(function (k) { return k + '=' + encodeURIComponent(hidden[k]); }).join('&');
      location.href = 'https://tally.so/r/' + FORM + (q ? '?' + q : '');
    }
  });
})();
