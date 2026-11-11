/* CLOSIMO findings: one industry at a time, bars grow in when shown */
(function(){
  var ps=document.querySelectorAll('.fp'),pn=document.querySelectorAll('.fpan');
  document.documentElement.classList.add('fjs');
  pn.forEach(function(p){p.removeAttribute('data-off')});
  function go(s){
    ps.forEach(function(p){var o=p.dataset.s===s;p.classList.toggle('on',o);p.setAttribute('aria-selected',o)});
    pn.forEach(function(p){var o=p.dataset.s===s;p.hidden=!o;p.classList.remove('grow');if(o){void p.offsetWidth;p.classList.add('grow')}});
  }
  ps.forEach(function(p){p.addEventListener('click',function(){go(p.dataset.s);p.scrollIntoView({block:'nearest',inline:'center',behavior:'smooth'})})});
  var first=document.querySelector('.fp.on');if(first)go(first.dataset.s);
})();
/* Touch screens: the card in the middle of the screen turns orange */
(function(){
  if(!('IntersectionObserver' in window)||matchMedia('(hover:hover)').matches)return;
  var io=new IntersectionObserver(function(es){es.forEach(function(e){e.target.classList.toggle('on',e.isIntersecting)})},{rootMargin:'-42% 0px -42% 0px'});
  document.querySelectorAll('.fc4').forEach(function(c){io.observe(c)});
})();
