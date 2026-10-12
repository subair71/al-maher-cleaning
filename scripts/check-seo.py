from pathlib import Path
import json
from urllib.parse import urlparse,unquote
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.tags=[];self.schema='';self.in_schema=False;self.main=False;self.h1=0;self.h2=0;self.p=0;self.scope=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs);self.tags.append((tag,a))
  if tag=='main':self.main=True
  if self.main:
   if tag=='h1':self.h1+=1
   if tag=='h2':self.h2+=1
   if tag=='p':self.p+=1
  if tag=='script' and a.get('type')=='application/ld+json':self.in_schema=True
  if tag=='section' and 'service-scope' in a.get('class',''):self.scope+=1
 def handle_endtag(self,tag):
  if tag=='main':self.main=False
  if tag=='script':self.in_schema=False
 def handle_data(self,data):
  if self.in_schema:self.schema+=data
 def has(self,tag):return any(t==tag for t,a in self.tags)
 def attrs(self,tag):return [a for t,a in self.tags if t==tag]
root=Path('.');count=0
for p in list(root.glob('*.html'))+list((root/'en').glob('*.html')):
 if p.name=='404.html':continue
 page=Page(p.read_text());rel=str(p)
 assert page.has('title'),rel
 assert any(a.get('name')=='description' for a in page.attrs('meta')),rel
 html=page.attrs('html')[0]
 assert html['lang']==('en' if rel.startswith('en/') else 'ar'),rel
 assert html['dir']==('ltr' if rel.startswith('en/') else 'rtl'),rel
 schema=json.loads(page.schema)
 assert not any(x.get('@type')=='AggregateRating' for x in schema['@graph']),rel
 if p.name not in ['admin.html','landing.html','service.html','review.html']:
  assert page.has('header') and page.has('footer'),rel
  assert page.h1==1,(rel,page.h1)
  if p.name.startswith('service-') or p.name=='index.html':assert page.h2>=1,rel
 for a in page.attrs('a'):
  h=a.get('href','');u=urlparse(h)
  if not h or u.scheme or h.startswith('#'):continue
  assert (root/unquote(u.path)).exists(),(rel,h)
 for img in page.attrs('img'):assert all(x in img for x in ['alt','width','height']),rel
 if p.name.startswith('service-'):assert page.scope==1 and page.p>=10,(rel,page.p)
 count+=1
sitemap=ET.parse('sitemap.xml');ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9','x':'http://www.w3.org/1999/xhtml'}
for item in sitemap.findall('s:url',ns):
 loc=item.find('s:loc',ns).text
 assert not any(x in loc for x in ['admin.html','quote.html','booking.html','campaigns/']),loc
 assert len(item.findall('x:link',ns))==3,loc
assert 'Disallow: /' not in Path('robots.txt').read_text()
assert 'name="robots" content="noindex"' in Path('404.html').read_text()
assert 'id="photos"' not in Path('quote.html').read_text()
print(f'PASS: {count} page language/heading/schema/image/link checks; sitemap, 404 and unsupported upload checks')
