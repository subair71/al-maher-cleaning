from pathlib import Path
import json,base64,re,mimetypes
r=Path('.')
assets={str(p):'data:'+str(mimetypes.guess_type(p)[0] or 'application/octet-stream')+';base64,'+base64.b64encode(p.read_bytes()).decode() for p in Path('assets').rglob('*') if p.suffix in ['.webp','.png','.woff2']}
css=Path('responsive-v3.css').read_text()
for p,u in assets.items():css=css.replace(p,u)
modules={str(p):p.read_text() for p in Path('js').rglob('*.js')}
a=modules['js/app.js']
a=a.replace("const image=(src,", "const image=(src,").replace('src="${esc(src)}"','src="${esc(globalThis.previewAsset(src))}"')
start=a.index('function currentPage()');end=a.index('\nfunction shell()',start)
a=a[:start]+"function currentPage(){return globalThis.previewPage||'index'}"+a[end:]
start=a.index('function navigate(url)');end=a.index('\nfunction captureDraft',start)
a=a[:start]+'''function navigate(url){captureDraft();const u=new URL(url,'https://preview.local/');const rel=u.pathname.replace(/^\\//,'');globalThis.previewPage=rel.replace(/^en\\//,'').replace(/\\.html$/,'')||'index';globalThis.previewSearch=u.search;if(u.pathname.startsWith('/en/'))setLanguage('en');if(['quote','booking','corporate'].includes(currentPage())){formDraft={service:u.searchParams.get('service')||(currentPage()==='corporate'?'corporate':'')};formErrors={};formMessage='';}render(true);scrollTo(0,0)}'''+a[end:]
start=a.index("$('#language').onclick=");end=a.index("$('.menu-toggle').onclick",start)
a=a[:start]+"$('#language').onclick=e=>{e.preventDefault();captureDraft();setLanguage(lang==='ar'?'en':'ar');render(false)};"+a[end:]
a=a.replace('location.search','(globalThis.previewSearch||\'\')')
a=a.replace("img.src=new URL(img.dataset.fallbackSrc||img.getAttribute('data-fallback')||'assets/cleaning-'+key+'.webp',document.baseURI).href", "img.src=globalThis.previewAsset(img.dataset.fallbackSrc||'assets/cleaning-'+key+'.webp')")
modules['js/app.js']=a
modules['js/platform/pages.js']=modules['js/platform/pages.js'].replace('src="${esc(url)}"','src="${esc(globalThis.previewAsset(url))}"')
# Keep existing external references in source; preview uses their existing local fallback assets.
init="""globalThis.previewPage='index';globalThis.previewAsset=src=>{if(ASSETS[src])return ASSETS[src];const photos=PHOTO;const key=Object.keys(photos).find(k=>photos[k]===src);return key?ASSETS['assets/cleaning-'+key+'.webp']||src:src};const cache={};function moduleURL(path){if(cache[path])return cache[path];let code=MODULES[path].replace(/from\s*['"]([^'"]+)['"]/g,(m,s)=>{const parts=path.split('/');parts.pop();for(const p of s.split('/')){if(p==='..')parts.pop();else if(p!=='.')parts.push(p)}return 'from '+JSON.stringify(moduleURL(parts.join('/')))});return cache[path]=URL.createObjectURL(new Blob([code],{type:'text/javascript'}))}import(moduleURL('js/app.js')).catch(e=>{document.getElementById('app').textContent=e.message});"""
# photos values are parsed from existing module without introducing assets.
photo_json=__import__('subprocess').check_output(['node','--input-type=module','-e',"import {photos} from './js/data.js';console.log(JSON.stringify(photos))"],text=True).strip()
script='const ASSETS='+json.dumps(assets)+';const PHOTO='+photo_json+';const MODULES='+json.dumps(modules)+';'+init
html='<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><base href="https://preview.local/"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Al Maher — branch review</title><style>'+css+'</style></head><body><div id="app"></div><script type="module">'+script.replace('</script','<\\/script')+'</script></body></html>'
Path('docs/branch-preview.html').write_text(html)
print('Offline interactive branch preview:',len(html),'bytes')
