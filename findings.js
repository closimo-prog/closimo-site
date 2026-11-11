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
/* Phones: swipe one card at a time. The card on screen turns orange and the counter follows */
(function(){
  var touch=!matchMedia('(hover:hover)').matches;
  document.querySelectorAll('.fpan').forEach(function(p){
    var g=p.querySelector('.fgrid5'),n=p.querySelector('.sw5 span');if(!g)return;
    var cs=g.querySelectorAll('.fc5');
    if(!('IntersectionObserver' in window))return;
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(touch)e.target.classList.toggle('on',e.isIntersecting);
      if(e.isIntersecting&&n)n.textContent=[].indexOf.call(cs,e.target)+1;
    })},{root:matchMedia('(min-width:760px)').matches?null:g,threshold:.6});
    cs.forEach(function(c){io.observe(c)});
  });
})();
