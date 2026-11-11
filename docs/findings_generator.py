import html,re
W='Where deals die'
# card: (headline, team, region, bars[(label,val,shown,hot)], big(value,label), kv[(k,v)], verdict)
D=[
('Real estate',[
 ('1,500 leads a month became 35 visits and 5 sales.','4 sales people','Pakistan',[('Leads a month',1500,'1,500',0),('Site visits',35,'35',0),('Sales',5,'5',1)],('PKR 1.5 Cr','lost a month'),[(W,'Between lead and site visit'),('Their target','100 visits a month · now 35'),('Average plot','PKR 1 Cr')],'1,465 buyers raised their hand and never saw the site. Your calls try to sell the plot. They should only sell the visit.'),
 ('200+ leads a month. Zero sales.',None,'Pakistan',[('Leads a month',200,'200+',0),('Sales',0,'0',1)],('0','sales from 200+ leads'),[(W,'At the ad'),('Their numbers','Click to WhatsApp ads, low intent buyers')],'Zero sales from 200 leads is not a sales team problem. Your ad invites browsers, not buyers.'),
]),
('Construction',[
 ('100 leads a month. 6 closed. 14 winnable deals lost.','3 sales people','Pakistan',[('Leads a month',100,'100',0),('Winnable deals lost',14,'14',1),('Deals closed',6,'6',0)],('PKR 42 Cr','lost a year'),[(W,'Waiting on the owner'),('Their target','25 deals a month · now 6'),('Their numbers','Owner handles every construction deal')],'Every big deal waits for the owner. The business can only close as many deals as one man has hours.'),
 ('500 leads became 30 customers. Half the closable deals lost.','3 sales people','Pakistan',[('Leads a month',500,'500',0),('Customers',30,'30',1)],('50%','of closable deals lost'),[(W,'At the price talk'),('Their numbers','Lost to price, rivals or a plumber'),('Average small job','PKR 10,000')],'Half your closable deals go to a cheaper quote or a plumber. When price is your only story, the cheapest one wins.'),
]),
('Solar',[
 ('36 deals won. Only 2 came from ads.','4 sales people','Pakistan',[('Won from referrals',34,'34',0),('Won from Meta ads',2,'2',1)],('PKR 1 Cr','stuck a month'),[(W,'After the quotation'),('Their numbers','6 deals a month'),('Average home system','PKR 15 lakh')],'Your engineers send strong quotes, then go quiet at the first objection. A crore a month sits there waiting for an answer.'),
 ('7 winnable deals lost every month.','3 sales people','Pakistan',[],('PKR 1 Cr','lost a month'),[(W,'In follow up'),('Their numbers','Everything in Google Sheets'),('Calls recorded','None')],'7 buyers a month were ready. No recording means nobody knows what was said when they walked away.'),
 ('500 leads a month. 20 worth calling.',None,'Pakistan',[('Leads a month',500,'500',0),('Qualified',20,'20',1)],('98%','of leads wasted'),[(W,'Before the first call'),('Their numbers','20 to 30 qualified a month')],'Your team spends 98% of the day on people who will never buy. Fix who you attract before you hire another caller.'),
]),
('Dental aligners',[
 ('700 leads became 30 patients.','6 sales people','Pakistan',[('Leads',700,'700',0),('Closed cases',30,'30',1)],('670','leads gone, no record why'),[(W,'Unknown. Lost deals are not tracked'),('Average treatment','PKR 1 lakh'),('Treatment length','8 to 10 months')],'670 people left and nobody wrote down why. You can\'t fix a leak you never look at.'),
]),
('Fertility (IVF) centre',[
 ('865 queries became 77 patients.','2 sales people','Pakistan',[('Queries last month',865,'865',0),('Became patients',77,'77',1)],('3 to 4 hrs','to reply to a new query'),[(W,'At the first reply'),('Ad spend','Up to PKR 25 lakh, results flat'),('First consultation','PKR 5,000')],'A patient who waits 4 hours has already called the next clinic. More ad money only buys more people to keep waiting.'),
]),
('ISO certification',[
 ('500 chats a day. 300 qualified. Follow ups missed.','6 sales people','Pakistan',[('Meta chats a day',500,'500',0),('Qualified',300,'300',1)],('300','qualified leads a day'),[(W,'In follow up'),('Main lost reason','Price'),('Average deal','PKR 1 lakh')],'300 qualified people a day and the follow up loses to meetings and breaks. The system should remember, not the rep.'),
]),
('Travel',[
 ('45 leads a day. 3% close. 70% of office visitors buy.','5 sales people','Pakistan',[('Leads a month',1350,'1,350',0),('Closed',40,'40',1)],('PKR 1.5 Cr','lost a month'),[(W,'Between chat and office visit'),('Their numbers','15 winnable deals lost a month'),('Average order','PKR 3 lakh per person')],'Your closing works. 7 in 10 visitors buy. The leak is the chat that never turns into a visit.'),
 ('1,000 leads a month. Under 2% book.','7 sales people','Pakistan',[('Leads a month',1000,'1,000',0),('Booked',20,'Under 20',1)],('PKR 25 lakh','gross profit lost a month'),[(W,'Between enquiry and booking'),('Their numbers','Under 2% close')],'1,000 people a month asked about a trip and fewer than 20 booked. That is not a lead problem. That is a selling problem.'),
 ('60 of 100 leads talk. 5 buy.','10 sales people','Pakistan',[('Leads',100,'100',0),('Became a discussion',60,'60',0),('Bought',5,'5',1)],('5%','close rate'),[(W,'After the 3rd follow up'),('Their numbers','Leads closed after 3 follow ups'),('Tracking','Google Sheets')],'6 in 10 leads want to talk. Your team stops after 3 follow ups and the office opens at 11 while leads arrive earlier.'),
 ('New deals fell from 80 a day to 50.','100 sales people','Pakistan',[('Before, per day',80,'80',0),('Now, per day',50,'50',1)],('30','fewer deals a day'),[(W,'In the pitch'),('Their numbers','5,000 leads a month'),('Lead cost','Up from $8 to $11')],'100 sellers and no shared pitch. Each team lead coaches his own way, so each team sells its own way.'),
]),
('Trade exhibitions',[
 ('20 companies interested per event. 5 booked.','8 sales people','Pakistan',[('Interested',20,'20',0),('Booked',5,'5',0),('Lost',15,'15',1)],('$1.35M','lost a year'),[(W,'Between interest and booking'),('Their numbers','15 of 20 lost per event'),('Average booth','$5,000')],'One rep sets the meeting, closes it and runs the event. He runs out of hours long before you run out of leads.'),
]),
('Software',[
 ('100 dials a day. 10 real talks. 10+ proposals lost a month.','4 sales people','Pakistan',[('Dials a day',100,'100',0),('Real conversations',10,'10',1)],('PKR 4 Cr','lost a month'),[(W,'After the proposal is emailed'),('Their numbers','10+ proposals lost a month'),('Average deal','PKR 40 lakh')],'You email a PKR 40 lakh proposal and wait. Nobody buys a deal that size from a PDF. Walk them through it live.'),
]),
('Fitness equipment',[
 ('400 leads a month. 6 sales.','15 sales people','Pakistan',[('Leads a month',400,'400',0),('Closed',6,'6',1)],('1.5%','close rate'),[(W,'In WhatsApp follow up'),('Their numbers','15 WhatsApp numbers, no CRM'),('Average order','PKR 1.75 lakh')],'15 reps, 15 WhatsApp numbers, no CRM. When a rep leaves, his customers leave with him.'),
]),
('Furniture showrooms',[
 ('Target PKR 5 Cr a month. Sales PKR 3 Cr.','4 showrooms','Pakistan',[('Monthly target',50,'PKR 5 Cr',0),('Actual sales',30,'PKR 3 Cr',1)],('PKR 1 Cr+','short every month'),[(W,'Between ad lead and showroom visit'),('Their numbers','70% of walk ins buy'),('Average order','PKR 1.5 lakh')],'7 in 10 people who walk in buy. Your sale is won at the showroom door. Every call should push people through it.'),
]),
('Gym',[
 ('Revenue PKR 70 lakh a month. Target PKR 1.4 Cr.',None,'Pakistan',[('Target',140,'PKR 1.4 Cr',0),('Revenue',70,'PKR 70 lakh',1)],('PKR 70 lakh','short every month'),[(W,'At the price talk'),('Their numbers','15% of enquiries join'),('Average membership','PKR 18,000')],'You are discounting your way to half your target. A cheaper price never fixed a weak pitch.'),
]),
('Education',[
 ('393 leads. Only 153 heard back the same day. 15 closed.',None,'Pakistan',[('Leads',393,'393',0),('Answered same day',153,'153',0),('Closed',15,'15',1)],('PKR 30 lakh','lost a month'),[(W,'At the first reply'),('Their target','8 to 10% close · now 3%'),('Lost a year','PKR 3.6 Cr')],'6 in 10 leads wait past day one. Your close rate fell from 8% to 3% right where the replies slowed down.'),
 ('30 leads a day. 1 in 5 deals lost to slow replies.','3 sales people','Pakistan',[('Deals',100,'100%',0),('Lost to slow replies',20,'20%',1)],('PKR 60 lakh','at risk if 2 reps leave'),[(W,'At the first reply'),('Their numbers','2 people do most of the selling'),('Average order','PKR 5,000')],'Your sales sit on 2 people. If they leave, PKR 60 lakh walks out with them.'),
]),
('Insurance',[
 ('2 in 100 leads close. Their target is 5.','22 agents','Pakistan',[('Target close rate',5,'5%',0),('Actual close rate',2,'2%',1)],('2%','close rate'),[(W,'In the agent pitch'),('Their target','5% close · now 2%'),('Their numbers','Agents are outsourced')],'Your agents are outsourced and so is your pitch. Nobody inside owns why 98 in 100 leads say no.'),
]),
('Immigration',[
 ('Closing at half the industry standard.','7 sales people','Pakistan',[('Industry standard',5,'5%',0),('Their close rate',2,'2%',1)],('2%','close rate'),[(W,'At counselling'),('Their target','5 to 10% · now 2 to 3%'),('Calls recorded','Yes, never used')],'You record every call and listen to none. The answer to your 2% is sitting in your own recordings.'),
]),
('Agencies',[
 ('15 sales meetings. Zero closes.',None,'Pakistan',[('Meetings in a month',15,'15',0),('Closes',0,'0',1)],('0','closes from 15 meetings'),[(W,'In the meeting'),('Their numbers','Buyers saw low value')],'15 meetings and 0 closes means buyers like you but don\'t see the value. That is an offer problem, not a lead problem.'),
 ('Same leads. The owner outsold 4 closers.','4 closers','Pakistan',[('Owner alone',15,'$15k a month',0),('4 closers together',10,'$10k a month',1)],('$15k','a month from the owner alone'),[(W,'In the closers\' calls'),('Their numbers','Same leads for everyone')],'Same leads, same offer, and you close more alone than 4 closers together. What you say on a call is written down nowhere.'),
]),
('Accounting',[
 ('Half the emailed proposals lost.',None,'UAE',[('Proposals emailed',100,'100%',0),('Lost',50,'50%',1)],('50%','of proposals lost'),[(W,'After the proposal is emailed'),('Their numbers','Proposals list features, not results')],'Your proposal lists services. Buyers want to see their problem solved. Half of them never reply.'),
 ('A $36k deal lost. Nobody asked why.',None,'UAE',[],('$36k','one deal lost'),[(W,'Unknown. No lost deal review')],'A $36k deal walked away and nobody asked why. The next one will leave for the same reason.'),
]),
('Facility management',[
 ('About 20 leads a month. Low conversion.','4 sales people','Pakistan',[('Small business leads',15,'15',0),('Enterprise leads',4,'4',1)],('PKR 10 lakh+','lost a month in new business'),[(W,'In follow up'),('Their numbers','Reps pulled into operations work')],'Your sellers do operations work. Every hour on a site is an hour no new client hears from you.'),
]),
('Online orders',[
 ('5,000 leads became 35 orders.',None,'Pakistan',[('Leads',5000,'5,000',0),('Orders',35,'35',1)],('0.7%','of leads bought'),[(W,'Between enquiry and order')],'5,000 people asked and 35 ordered. Before you buy more leads, find out what the other 4,965 heard.'),
]),
('Distribution',[
 ('1,600 customers down to 400.','5 order bookers','Pakistan',[('Customers before',1600,'1,600',0),('Customers now',400,'400',1)],('PKR 1 Cr+','lost'),[(W,'In collections'),('Their numbers','90% credit market'),('Cash cycle','4 months')],'Credit grew faster than profit, so 1,200 customers had to go. Credit only sells when someone collects.'),
 ('PKR 2.5 Cr sold a month. PKR 4.5 Cr stuck with customers.','5 sales people','Pakistan',[('Sales a month',25,'PKR 2.5 Cr',0),('Stuck in receivables',45,'PKR 4.5 Cr',1)],('PKR 4.5 Cr','stuck in receivables'),[(W,'In collections'),('Their numbers','95% of sales on credit'),('Payment time','60 to 100 days')],'You sell PKR 2.5 Cr a month and PKR 4.5 Cr sits with customers. Your sales team is running a free bank.'),
 ('75% of sales time spent on admin.',None,'Pakistan',[('Sales time',100,'100%',0),('Spent on admin',75,'75%',1)],('75%','of sales time on admin'),[(W,'Before the sale starts'),('Their numbers','Order takers, not sellers')],'Your sales people spend 3 of every 4 hours on paperwork. You are paying sellers to be clerks.'),
 ('20% of customers bring 80% of revenue.',None,'Pakistan',[('Share of customers',20,'Top 20%',0),('Share of revenue',80,'80%',1)],('80%','of revenue from 20% of customers'),[(W,'After the first order'),('Their numbers','No cross selling')],'Your best 20% bring 80% of the money and nobody sells them a second product.'),
]),
('Corporate sales',[
 ('Revenue fell from PKR 1.7 Cr to 1.1 Cr a month.',None,'Pakistan',[('Before, a month',17,'PKR 1.7 Cr',0),('Now, a month',11,'PKR 1.1 Cr',1)],('PKR 60 lakh','less every month'),[(W,'Unknown. No view of stalled deals')],'Revenue fell by PKR 60 lakh a month and nobody can say which deals stalled or why.'),
]),
('Wires and cables',[
 ('100 leads. 10 close.','6 sales people','Pakistan',[('Leads',100,'100',0),('Closed',10,'10',1)],('2 days','before a new lead hears back'),[(W,'Waiting on the CEO'),('Their numbers','CEO approves every quote'),('Revenue swing','PKR 1 Cr to 10 Cr a month')],'Every quote waits for the CEO and every lead waits 2 days. The business moves at the speed of one inbox.'),
]),
]
def esc(x): return html.escape(x,quote=True)
def card(ind,f):
    h,tm,rg,bars,big,kv,v=f
    mx=max([b[1] for b in bars] or [1]) or 1
    rows=''.join('<div class="br5%s"><span>%s</span><b>%s</b><div class="t5"><i style="--w:%.1f%%"></i></div></div>'%(' hot' if hot else '',esc(l),esc(s),max(2,100*v/mx) if v else 0) for l,v_,s,hot in [(b[0],b[1],b[2],b[3]) for b in bars] for v in [v_])
    o='<article class="fc5" tabindex="0"><div class="tp5"><b>%s · %s</b>%s</div><h3>%s</h3>'%(esc(ind),rg,'<span>%s</span>'%esc(tm) if tm else '',esc(h))
    if rows: o+='<div class="bs5">'+rows+'</div>'
    o+='<div class="ls5"><strong>%s</strong><span>%s</span></div>'%(esc(big[0]),esc(big[1]))
    o+='<dl class="kv5">'+''.join('<div><dt>%s</dt><dd>%s</dd></div>'%(esc(a),esc(b)) for a,b in kv)+'</dl>'
    o+='<div class="vd5"><span>Our verdict</span><p>%s</p></div></article>'%esc(v)
    return o
def slug(x): return re.sub(r'[^a-z]+','-',x.lower()).strip('-')
pills=''.join('<button class="fp%s" role="tab" aria-selected="%s" data-s="%s">%s <span>%d</span></button>'%(' on' if i==0 else '','true' if i==0 else 'false',slug(n),esc(n),len(fs)) for i,(n,fs) in enumerate(D))
panels=''.join('<div class="fpan" role="tabpanel" data-s="%s"%s><div class="fgrid5">%s</div>%s</div>'%(slug(n),'' if i==0 else ' data-off',''.join(card(n,f) for f in fs),'<p class="sw5"><span>1</span> of %d · swipe →</p>'%len(fs) if len(fs)>1 else '') for i,(n,fs) in enumerate(D))
total=sum(len(fs) for _,fs in D)
sec='''  <section class="fh">
    <a class="back" href="../">← Back to home</a>
    <h1>40+ businesses we diagnosed since July 2026.</h1>
    <p>Their numbers, in their words. Where the deals die, what it costs them, and our verdict. Industry only, because every client is under NDA.</p>
  </section>
  <section class="s fsel" id="all">
    <div class="fbar" role="tablist" aria-label="Pick an industry">'''+pills+'''</div>
    <div class="fpans">'''+panels+'''</div>
  </section>
'''
s=open('findings/index.html').read()
i=s.index('  <section class="fh">');j=s.index('  <section class="final">')
s=s[:i]+sec+s[j:]
open('findings/index.html','w').write(s)
print('cards',total,'industries',len(D))
