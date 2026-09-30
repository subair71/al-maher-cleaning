const services=[
['s4.png','تنظيف المنازل والشقق','Home & apartment cleaning','عناية شاملة بالشقق المفروشة والمنازل والفلل، من الغرف إلى المطابخ.','Complete care for furnished apartments, homes and villas, from rooms to kitchens.'],
['s8.png','دراي كلين الكنب والسجاد','Sofa & carpet cleaning','تنظيف الكنب والسجاد والمفروشات لإطلالة منتعشة ومكان أريح.','Refresh sofas, carpets and upholstery for a more comfortable space.'],
['s5.png','تنظيف ما بعد البناء','Post-construction cleaning','إزالة آثار أعمال البناء والتشطيب وتجهيز المكان لبداية جديدة.','Clear away the traces of building and finishing work for a fresh start.'],
['s7.png','تنظيف الزجاج والشبابيك','Window & glass cleaning','عناية بالزجاج والشبابيك لإطلالة صافية ولمعان يكمّل نظافة المكان.','Care for windows and glass for a clear view and a polished finish.'],
['s6.png','التنظيف العميق','Deep cleaning','اهتمام بالتفاصيل في المطابخ والزوايا والمساحات التي تحتاج عناية إضافية.','Extra attention for kitchens, corners and areas that need a deeper clean.'],
['s3.png','تنظيف المكاتب والشركات','Office & business cleaning','مساحات عمل نظيفة ومرتبة، بخدمة تتناسب مع احتياجات منشأتك.','Clean, welcoming workplaces with a service tailored to your business.']];
const paths=[
'<path d="m3 10 9-7 9 7v11H3Z"/><path d="M9 21v-8h6v8"/>',
'<rect x="4" y="9" width="16" height="10" rx="3"/><path d="M7 9V5h10v4M4 13h16M6 19v2m12-2v2"/>',
'<path d="M4 21h16M7 21V9h10v12M5 9l7-6 7 6M10 13h4M10 17h4"/>',
'<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M12 3v18M4 12h16"/>',
'<path d="M12 3 4 6v6c0 5 8 9 8 9s8-4 8-9V6Z"/><path d="m8 12 3 3 5-6"/>',
'<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h1m4 0h1m-6 4h1m4 0h1m-6 4h1m4 0h1M10 21v-3h4v3"/>'
];
const grid=document.getElementById('service-grid');
grid.innerHTML=services.map((s,i)=>`<article class="service"><div class="service-icon"><svg viewBox="0 0 24 24" aria-hidden="true">${paths[i]}</svg></div><div class="service-body"><h3 data-ar="${s[1]}" data-en="${s[2]}"></h3><p data-ar="${s[3]}" data-en="${s[4]}"></p><a class="wa text-link" data-service-ar="${s[1]}" data-service-en="${s[2]}" data-ar="اعرف المزيد" data-en="Learn more"></a></div></article>`).join('');
document.getElementById('footer-services').innerHTML=services.map(s=>`<a href="#services" data-ar="${s[1]}" data-en="${s[2]}"></a>`).join('');
let lang='ar';try{lang=localStorage.getItem('maher-language')==='en'?'en':'ar'}catch{}
function render(){document.documentElement.lang=lang;document.documentElement.dir=lang==='ar'?'rtl':'ltr';document.querySelectorAll('[data-ar][data-en]').forEach(el=>el.innerHTML=el.dataset[lang]);document.querySelectorAll('.wa').forEach(el=>{const service=el.dataset[lang==='ar'?'serviceAr':'serviceEn'];const message=lang==='ar'?'مرحباً شركة الماهر، أرغب في الاستفسار عن '+(service||'خدمات التنظيف والحصول على عرض سعر')+'.':'Hello Al Maher, I would like to enquire about '+(service||'your cleaning services and request a quote')+'.';el.href='https://wa.me/962778842130?text='+encodeURIComponent(message);el.target='_blank';el.rel='noopener noreferrer'});document.getElementById('language').innerHTML=lang==='ar'?'English ◎':'العربية ◎';document.getElementById('language').setAttribute('aria-label',lang==='ar'?'Switch to English':'التبديل إلى العربية');document.title=lang==='ar'?'الماهر | خدمات التنظيف والدراي كلين':'Al Maher | Cleaning & Dry Cleaning';const select=document.getElementById('service-select');const selected=select.value;select.innerHTML='<option value="">'+(lang==='ar'?'اختر الخدمة':'Choose a service')+'</option>'+services.map((s,i)=>'<option value="'+i+'">'+s[lang==='ar'?1:2]+'</option>').join('');select.value=selected}
document.getElementById('language').onclick=()=>{lang=lang==='ar'?'en':'ar';try{localStorage.setItem('maher-language',lang)}catch{}render()};render();

const menu=document.getElementById('menu-toggle'),nav=document.getElementById('main-nav');
menu.onclick=()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));menu.textContent=open?'×':'☰'};
nav.querySelectorAll('a').forEach(a=>a.onclick=()=>{nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.textContent='☰'});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');menu.textContent='☰'}});
document.getElementById('enquiry').onsubmit=e=>{e.preventDefault();const d=new FormData(e.currentTarget);const ar=lang==='ar';const msg=(ar?'مرحباً شركة الماهر، أود الاستفسار عن خدمة تنظيف.':'Hello Al Maher, I would like to enquire about cleaning.')+'\n'+(ar?'الاسم: ':'Name: ')+d.get('name')+'\n'+(ar?'الهاتف: ':'Phone: ')+d.get('phone')+'\n'+(ar?'الخدمة: ':'Service: ')+services[Number(d.get('service'))][ar?1:2]+'\n'+(ar?'الرسالة: ':'Message: ')+d.get('message');window.open('https://wa.me/962778842130?text='+encodeURIComponent(msg),'_blank','noopener,noreferrer')};

const motionPreference=matchMedia('(prefers-reduced-motion: reduce)');
if('IntersectionObserver' in window&&!motionPreference.matches){
 const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{
  if(entry.isIntersecting){entry.target.classList.add('motion-enter');observer.unobserve(entry.target)}
 }),{threshold:.08});
 document.querySelectorAll('.section-heading,.about,.why-picture,.benefit,.service,.offers article,.gallery figure,.steps article,.cta-band .wrap,#enquiry').forEach(el=>{
  const siblings=Array.from(el.parentElement.children);
  el.style.setProperty('--motion-delay',Math.min(siblings.indexOf(el),3)*65+'ms');
  observer.observe(el);
 });
 motionPreference.addEventListener('change',event=>{if(event.matches){observer.disconnect();document.querySelectorAll('.motion-enter').forEach(el=>el.classList.remove('motion-enter'))}});
}
