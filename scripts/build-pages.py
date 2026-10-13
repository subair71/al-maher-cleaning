from pathlib import Path
from html import escape
import json
pages={'index':('الماهر | خدمات التنظيف والدراي كلين','Al Maher | Cleaning & Dry Cleaning'),'services':('خدماتنا','Our services'),'about':('من نحن','About Al Maher'),'gallery':('أعمالنا','Our work'),'offers':('العروض','Offers'),'contact':('تواصل معنا','Contact'),'quote':('طلب عرض سعر','Request a quote'),'booking':('طلب حجز','Booking request'),'faq':('الأسئلة الشائعة','FAQs'),'privacy':('سياسة الخصوصية','Privacy policy'),'terms':('الشروط والأحكام','Terms and conditions'),'admin':('لوحة الإدارة','Admin dashboard'),'service':('تفاصيل الخدمة','Service details'),'corporate':('خدمات وعقود تنظيف الشركات','Corporate & contract cleaning'),'review':('شارك تجربتك','Share your experience'),'landing':('خدمات الماهر','Al Maher services')}
pages['cleaning-guide']=('دليل التحضير للتنظيف','Cleaning preparation guide')
services={'home':('تنظيف المنازل والشقق','Home & apartment cleaning'),'sofa':('دراي كلين الكنب والسجاد','Sofa & carpet cleaning'),'construction':('تنظيف ما بعد البناء','Post-construction cleaning'),'glass':('تنظيف الزجاج والشبابيك','Window & glass cleaning'),'deep':('التنظيف العميق','Deep cleaning'),'office':('تنظيف المكاتب والشركات','Office & business cleaning'),'villa':('تنظيف الفلل','Villa cleaning'),'apartment':('تنظيف الشقق','Apartment cleaning'),'car':('دراي كلين السيارات','Car interior dry cleaning'),'tank':('تنظيف خزانات المياه','Water tank cleaning'),'corporate':('عقود تنظيف الشركات','Corporate cleaning contracts')}
slugs={'post-construction-cleaning':'construction','sofa-cleaning':'sofa','villa-cleaning':'villa','apartment-cleaning':'apartment','car-dry-cleaning':'car','water-tank-cleaning':'tank','corporate-cleaning-contracts':'corporate'}
routes={p+'.html':titles for p,titles in pages.items()}
routes.update({'service-'+k+'.html':v for k,v in services.items()})
routes.update({'campaigns/'+slug+'/index.html':services[key] for slug,key in slugs.items()})
routes['offers/sofa-cleaning/index.html']=services['sofa']
routes['services/villa-cleaning/index.html']=services['villa']
import os, subprocess
from urllib.parse import urljoin
from xml.sax.saxutils import escape as xml_escape
base=os.environ.get('SEO_BASE_URL','https://subair71.github.io/al-maher-cleaning/').rstrip('/')+'/'
preview=os.environ.get('SEO_PREVIEW','0')=='1'
data=json.loads(subprocess.check_output(['node','--input-type=module','-e',"import {services} from './js/data.js';import {serviceFaqs} from './js/rich-content.js';import {repository as db} from './js/repository.js';console.log(JSON.stringify({serviceFaqs:Object.fromEntries(db.list('services').map(s=>[s.id,serviceFaqs(s.id)])),services:db.list('services'),faqs:db.list('faqs').filter(f=>f.status==='published').map(f=>[f.title,f.description])}))"],text=True))
service_data={s['id']:s for s in data['services']}
rendered=json.loads(subprocess.check_output(['node','scripts/render-static.mjs',json.dumps(list(routes))],text=True))
private={'admin.html','service.html','landing.html','quote.html','booking.html','review.html'}
metadata={}; sitemap=[]
for language in ['ar','en']:
 for path,titles in routes.items():
    output=('en/' if language=='en' else '')+path
    url=base+output
    canonical_path=path
    if path.startswith(('campaigns/','offers/','services/')):
        alias_key=slugs.get(path.split('/')[1], 'sofa' if path.startswith('offers/') else None)
        if alias_key:canonical_path='service-'+alias_key+'.html'
    if canonical_path=='index.html':canonical_path=''
    url=base+('en/' if language=='en' else '')+canonical_path
    ar_url=base+canonical_path; en_url=base+'en/'+canonical_path
    key=path.removeprefix('service-').removesuffix('.html') if path.startswith('service-') else slugs.get(path.split('/')[1] if '/' in path else '')
    details=service_data.get(key,{})
    title=titles[0 if language=='ar' else 1]
    if path=='index.html':title='تنظيف المنازل والكنب والمكاتب' if language=='ar' else 'Home, sofa & office cleaning'
    title=(title+' في الرصيفة والزرقاء وعمّان | الماهر') if language=='ar' else (title+' in Russeifa, Zarqa & Amman | Al Maher')
    description=details.get('description',{}).get(language) or (titles[0]+' من الماهر في الرصيفة والزرقاء وعمّان. تواصل معنا لمناقشة احتياجات المكان وتأكيد نطاق الخدمة والسعر والموعد.' if language=='ar' else titles[1]+' from Al Maher in Russeifa, Zarqa and Amman, Jordan. Discuss your space, service scope, pricing and visit with our local team.')
    if details:description=details['title'][language]+(' من الماهر في الرصيفة والزرقاء وعمّان. ناقش نطاق الخدمة والسعر والتحضير والموعد.' if language=='ar' else ' from Al Maher in Russeifa, Zarqa and Amman. Explore scope, quote details, preparation and booking requests.')
    metadata[output]={'title':title,'description':description,'canonical':url,'ar':ar_url,'en':en_url}
    business={'@type':'LocalBusiness','@id':base+'#business','name':'Al Maher Cleaning & Dry Cleaning','alternateName':'الماهر لخدمات التنظيف والدراي كلين','url':base,'telephone':'+962778842130','logo':base+'assets/s1.png','image':base+'assets/cleaning-hero.webp','address':{'@type':'PostalAddress','streetAddress':'Jabal Al Shamali, King Abdullah II Street','addressLocality':'Russeifa','addressCountry':'JO'},'areaServed':[{'@type':'City','name':n} for n in ['Russeifa','Zarqa','Amman']]}
    graph=[business,{'@type':'WebSite','@id':base+'#website','url':base,'name':'Al Maher','publisher':{'@id':base+'#business'},'inLanguage':['ar-JO','en']},{'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':description,'inLanguage':'ar-JO' if language=='ar' else 'en','isPartOf':{'@id':base+'#website'},'about':{'@id':base+'#business'}},{'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'الرئيسية' if language=='ar' else 'Home','item':base+('en/' if language=='en' else '')+'index.html'}]+([] if path=='index.html' else [{'@type':'ListItem','position':2,'name':titles[0 if language=='ar' else 1],'item':url}])}]
    if details:graph.append({'@type':'Service','@id':url+'#service','name':details['title'][language],'description':description,'provider':{'@id':base+'#business'},'areaServed':business['areaServed'],'url':url})
    if details and path.startswith('service-'):
        questions=data['serviceFaqs'].get(key,[])+data['faqs'][:3]
        graph.append({'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q[0][language],'acceptedAnswer':{'@type':'Answer','text':q[1][language]}} for q in questions]})
    if path=='faq.html':graph.append({'@type':'FAQPage','mainEntity':[{'@type':'Question','name':q[0][language],'acceptedAnswer':{'@type':'Answer','text':q[1][language]}} for q in data['faqs']]})
    schema=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('</','<\/')
    metadata[output]['schema']={'@context':'https://schema.org','@graph':graph}
    root_relative='../'*(len(Path(output).parts)-1) or './'
    links=''.join(f'<li><a href="{("en/" if language=="en" else "")}service-{k}.html">{escape(v["title"][language])}</a><p>{escape(v["description"][language])}</p></li>' for k,v in service_data.items())
    faq_content=''.join(f'<details><summary>{escape(q[0][language])}</summary><p>{escape(q[1][language])}</p></details>' for q in data['faqs']) if path=='faq.html' else ''
    static=f'<main id="main" class="wrap section"><h1>{escape(title)}</h1><p>{escape(description)}</p><p>{"خدمات التنظيف للمنازل والمكاتب والمفروشات في الأردن" if language=="ar" else "Home, office and upholstery cleaning in Jordan"}</p><ul>{links}</ul>{faq_content}<a href="tel:+962778842130">+962 77 884 2130</a> <a href="https://wa.me/962778842130">WhatsApp</a></main>'
    static=rendered.get(output,static)
    static='<noscript><p class="wrap scope-note">'+('لإعداد النموذج فعّل JavaScript، أو تواصل مباشرة عبر واتساب أو الهاتف.' if language=='ar' else 'Enable JavaScript to prepare forms, or contact us directly by WhatsApp or phone.')+'</p></noscript>'+static
    robots='noindex,follow' if preview or path in private or path.startswith(('campaigns/','offers/','services/')) else 'index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'
    metadata[output]['robots']=robots
    text=f'''<!doctype html><html lang="{language}" dir="{'rtl' if language=='ar' else 'ltr'}"><head><meta charset="utf-8"><base href="{root_relative}"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#14375c"><meta name="robots" content="{robots}"><title>{escape(title)}</title><meta name="description" content="{escape(description)}"><link rel="canonical" href="{url}"><link rel="alternate" hreflang="ar-JO" href="{ar_url}"><link rel="alternate" hreflang="en" href="{en_url}"><link rel="alternate" hreflang="x-default" href="{ar_url}"><meta property="og:type" content="website"><meta property="og:site_name" content="Al Maher"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(description)}"><meta property="og:url" content="{url}"><meta property="og:locale" content="{'ar_JO' if language=='ar' else 'en_JO'}"><meta property="og:image" content="{base}assets/cleaning-hero.webp"><meta name="twitter:card" content="summary_large_image"><meta property="og:image:alt" content="{'صورة توضيحية لخدمات التنظيف' if language=='ar' else 'Illustrative cleaning service photograph'}"><meta property="og:locale:alternate" content="{'en_JO' if language=='ar' else 'ar_JO'}"><link rel="preload" href="assets/fonts/{'noto-sans-arabic' if language=='ar' else 'dm-sans'}-400.woff2" as="font" type="font/woff2" crossorigin><link rel="stylesheet" href="responsive-v3.css"><script type="application/ld+json">{schema}</script></head><body><div id="app">{static}</div><script type="module" src="js/app.js"></script></body></html>'''
    target=Path(output);target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text)
    if path not in private and not path.startswith(('campaigns/','offers/','services/')):sitemap.append((url,ar_url,en_url))
Path('js/seo-data.js').write_text('export const seoPages='+json.dumps(metadata,ensure_ascii=False)+';\n')
Path('sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+''.join('<url><loc>'+xml_escape(url)+'</loc>'+''.join(f'<xhtml:link rel="alternate" hreflang="{lang}" href="{xml_escape(href)}"/>' for lang,href in [('ar-JO',ar),('en',en),('x-default',ar)])+'</url>' for url,ar,en in sitemap)+'</urlset>')
Path('robots.txt').write_text('User-agent: *\n'+('Disallow: /\n' if preview else 'Allow: /\n')+'Sitemap: '+base+'sitemap.xml\n')

not_found='<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>الصفحة غير موجودة | Al Maher</title></head><body><main><h1>الصفحة غير موجودة / Page not found</h1><p><a href="'+base+'">الرئيسية / Home</a></p><p><a href="'+base+'en/">English</a></p></main></body></html>'
Path('404.html').write_text(not_found)
