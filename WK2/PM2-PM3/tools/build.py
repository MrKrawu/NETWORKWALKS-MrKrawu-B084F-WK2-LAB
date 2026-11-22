import zipfile, html, re, sys
from xml.etree import ElementTree as ET
import os
B=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data')+'/'
NS={'t':'urn:oasis:names:tc:opendocument:xmlns:table:1.0','x':'urn:oasis:names:tc:opendocument:xmlns:text:1.0','x2':'urn:oasis:names:tc:opendocument:xmlns:text:1.0'}
T='{urn:oasis:names:tc:opendocument:xmlns:table:1.0}'
X='{urn:oasis:names:tc:opendocument:xmlns:text:1.0}'
def cell_text(c):
    return ' '.join(''.join(p.itertext()).strip() for p in c.iter(X+'p')).strip()
def read(odt):
    root=ET.fromstring(zipfile.ZipFile(odt).read('content.xml'))
    rows=[]
    for r in root.iter(T+'table-row'):
        row=[cell_text(c) for c in r if c.tag==T+'table-cell']
        if any(row): rows.append(row)
    return rows[0],rows[1:]
def tbl(odt, kind):
    head,rows=read(odt)
    out='<table class="d"><tr><th class="n">No.</th><th>Link</th><th>Relevant Dork</th><th class="c">Credentials</th></tr>'
    for r in rows:
        r=(r+['']*4)[:4]
        num,link,dork,cred=r
        link_h=f'<a href="{html.escape(link)}">{html.escape(link)}</a>'
        dork_h=f'<code>{html.escape(dork)}</code>' if dork else '–'
        out+=f'<tr><td class="n">{html.escape(num)}</td><td class="l">{link_h}</td><td>{dork_h}</td><td class="c">{html.escape(cred) or "–"}</td></tr>'
    return out+'</table>', len(rows)
cams,nc=tbl(B+'List_webcams.odt','cam')
books,nb=tbl(B+'List_ebooks.odt','book')
print(nc,nb)
tpl=open(sys.argv[1]).read().replace('@@CAMS@@',cams).replace('@@BOOKS@@',books)
open(sys.argv[2],'w').write(tpl)
