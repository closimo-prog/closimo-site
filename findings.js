/* CLOSIMO findings filter: shows one industry group or all */
(function(){var ps=document.querySelectorAll('.fp'),gs=document.querySelectorAll('.fgrp'),c=document.getElementById('cnt');
ps.forEach(function(p){p.addEventListener('click',function(){var s=p.dataset.s,n=0;ps.forEach(function(q){q.classList.toggle('on',q===p);q.setAttribute('aria-pressed',q===p)});
gs.forEach(function(g){var v=s==='all'||g.dataset.s===s;g.hidden=!v;if(v)n+=g.querySelectorAll('.fc').length});c.textContent=s==='all'?'Showing all '+n:'Showing '+n+' in '+s})})})();
