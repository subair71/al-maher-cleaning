import fs from 'node:fs';
import vm from 'node:vm';
globalThis.document={documentElement:{lang:'ar',dir:'rtl'}};
const data=await import('../js/data.js');
const i18n=await import('../js/i18n.js');
const {repository:db}=await import('../js/repository.js');
const logic=await import('../js/logic.js');
const platform=await import('../js/platform/pages.js');
const rich=await import('../js/rich-content.js');
const copy=await import('../js/section-copy.js');
const {config}=await import('../js/config.js');
const app=fs.readFileSync('js/app.js','utf8').split('function render(focus=false)')[0].replace(/^import .*;\n/gm,'');
const out={};
const routes=JSON.parse(process.argv[2]);
for(const language of ['ar','en']){
 i18n.setLanguage(language);
 for(const route of routes){
  const page=route==='index.html'?'home':route.replace('.html','');
  const context=vm.createContext({...data,...platform,...rich,...copy,db,config,lang:language,t:i18n.t,w:i18n.w,esc:logic.escapeHTML,URL,URLSearchParams,document:{querySelector:()=>null},location:{search:'',pathname:'/'+route}});
  vm.runInContext(app,context);
  let expression=page==='home'?'home()':page==='services'?'servicesPage()':page.startsWith('service-')?`servicePage(${JSON.stringify(page.slice(8))})`:page==='about'?'aboutPage()':page==='gallery'?'galleryPage()':page==='contact'?'contactPage()':page==='cleaning-guide'?`intro(tr('دليل التحضير للتنظيف','Plan your clean'),tr('تفاصيل تساعد على التخطيط للزيارة.','Practical guidance for planning your visit.'))+guideContent(lang)+cta()`:page==='faq'?`intro(w('faq'),tr('إجابات تساعدك على التخطيط.','Answers to help you plan.'))+'<section class="wrap section tight legal">'+faqBlock()+'</section>'`:page==='offers'?`intro(w('offers'),tr('يرجى تأكيد التوفر والشروط.','Please confirm availability and terms.'))+'<section class="wrap section tight"><div class="grid three">'+offerCards()+'</div></section>'`:['privacy','terms'].includes(page)?`legalPage('${page}')`:['quote','booking','corporate'].includes(page)?`formPage('${page}')`:null;
  if(!expression)continue;
  vm.runInContext(`page=${JSON.stringify(page)}`,context);
  const content=vm.runInContext(expression,context);
  let html=vm.runInContext('shell()',context).replace('<main id="main" tabindex="-1"></main>',`<main id="main" tabindex="-1" class="${page==='home'?'design-home':''}">${content}</main>`);
  // All static navigation works before JS runs; base is the repository root.
  if(language==='en')html=html.replace(/href="((?!https?:|tel:|#)[^"]+)"/g,(m,h)=>`href="en/${h}"`);
  html=html.replace(/<button class="language" id="language">.*?<\/button>/,`<a class="language" id="language" href="${language==='en'?'':'en/'}${route}">${language==='en'?'العربية':'English'}</a>`);
  out[(language==='en'?'en/':'')+route]=html;
 }
}
process.stdout.write(JSON.stringify(out));
