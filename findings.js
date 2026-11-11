/* CLOSIMO findings filter */
(function(){var ps=document.querySelectorAll('.fp'),cs=document.querySelectorAll('.fc'),c=document.getElementById('cnt');
ps.forEach(function(p){p.addEventListener('click',function(){var s=p.dataset.s,n=0;ps.forEach(function(q){q.classList.toggle('on',q===p);q.setAttribute('aria-pressed',q===p)});
cs.forEach(function(k){var v=s==='all'||k.dataset.s===s;k.hidden=!v;if(v)n++});c.textContent=s==='all'?'Showing all '+n:'Showing '+n+' in '+s})})})();
