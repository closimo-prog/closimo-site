/* CLOSIMO home page v2 */
(function(){var b=document.getElementById('mbar'),h=document.querySelector('.hero .btns');if(!('IntersectionObserver' in window)||!h)return;new IntersectionObserver(function(e){b.classList.toggle('on',!e[0].isIntersecting&&e[0].boundingClientRect.top<0)}).observe(h)})();
(function(){var bs=document.querySelectorAll('.seg button'),v=document.getElementById('pval');bs.forEach(function(b){b.addEventListener('click',function(){bs.forEach(function(x){x.setAttribute('aria-checked',x===b)});v.textContent=b.dataset.p})})})();
(function(){document.querySelectorAll('.xh').forEach(function(b){b.addEventListener('click',function(){var c=b.parentNode,o=!c.classList.contains('open');c.classList.toggle('open',o);b.setAttribute('aria-expanded',o)})})})();
(function(){var q=document.querySelector('.quotes'),d=document.getElementById('qdots');if(!q||!d)return;var f=q.querySelectorAll('figure');f.forEach(function(){d.appendChild(document.createElement('i'))});var ds=d.children;function u(){var c=q.scrollLeft+q.clientWidth/2,b=0,m=1e9;f.forEach(function(x,i){var k=Math.abs(x.offsetLeft+x.offsetWidth/2-c);if(k<m){m=k;b=i}});for(var i=0;i<ds.length;i++)ds[i].className=i===b?'on':''}q.addEventListener('scroll',u,{passive:true});u()})();
(function(){var bs=document.querySelectorAll('.ab'),ps=document.querySelectorAll('.apn');function go(i){bs.forEach(function(b,k){var o=k===i;b.classList.toggle('on',o);b.setAttribute('aria-selected',o)});ps.forEach(function(p,k){p.hidden=k!==i;p.classList.toggle('on',k===i)})}bs.forEach(function(b,i){b.addEventListener('click',function(){go(i)});if(window.matchMedia('(hover:hover)').matches)b.addEventListener('mouseenter',function(){go(i)})})})();
/* Paid Audit: price by market, tier price on the button, and every Paid Audit button goes to the pricing card first */
(function(){
  var tz='';try{tz=Intl.DateTimeFormat().resolvedOptions().timeZone||''}catch(e){}
  var pk=(tz==='Asia/Karachi');
  var bs=document.querySelectorAll('.seg button'),v=document.getElementById('pval'),pn=document.querySelector('#paybtn .pnow'),pf=document.querySelector('.pfrom');
  function price(b){return pk?b.dataset.p:b.dataset.usd}
  function sync(){var b=document.querySelector('.seg button[aria-checked="true"]')||bs[0];if(!b)return;var p=price(b);if(v)v.textContent=p;if(pn){pn.textContent='\u00a0· '+p;pn.parentNode.classList.toggle('custom',p==='Fully custom')}}
  if(!pk&&pf)pf.textContent='$750';
  bs.forEach(function(b){b.addEventListener('click',sync)});sync();
  var card=document.getElementById('paid');
  function go(e){if(e)e.preventDefault();if(!card)return;card.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'center'});card.classList.remove('pulse');void card.offsetWidth;card.classList.add('pulse')}
  document.addEventListener('click',function(e){var a=e.target.closest('[data-go="audit"]');if(a)go(e)});
  if(location.hash==='#paid')setTimeout(go,300);
  window.closimoPrice=function(){var b=document.querySelector('.seg button[aria-checked="true"]');return b?price(b):''};
})();
