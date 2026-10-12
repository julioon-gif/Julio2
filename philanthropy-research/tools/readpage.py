#!/usr/bin/env python3
"""Usage: readpage.py URL [keyword ...]  -> prints page text (HTML or PDF), or windows around keywords."""
import sys, subprocess, re, html, tempfile, os
url=sys.argv[1]; kws=[k.lower() for k in sys.argv[2:]]
with tempfile.NamedTemporaryFile(delete=False) as f: path=f.name
r=subprocess.run(["curl","-sL","-m","40","-A","Mozilla/5.0 (Windows NT 10.0; Win64; x64)","-o",path,"-w","%{http_code} %{content_type}",url],capture_output=True,text=True)
print("HTTP",r.stdout)
data=open(path,'rb').read()
if data[:4]==b'%PDF':
    t=subprocess.run(["pdftotext","-layout",path,"-"],capture_output=True,text=True).stdout
else:
    t=data.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style|noscript).*?</\1>','',t)
    t=html.unescape(re.sub(r'<[^>]+>','\n',t))
lines=[re.sub(r'\s+',' ',l).strip() for l in t.splitlines()]
txt='\n'.join(l for l in lines if l)
os.unlink(path)
if not kws: print(txt[:12000]); sys.exit()
low=txt.lower(); shown=0
for k in kws:
    for m in re.finditer(re.escape(k),low):
        print(f"--- [{k}] ---\n"+txt[max(0,m.start()-600):m.start()+900]); shown+=1
        if shown>12: sys.exit()
if not shown: print("(no keyword hits)\n"+txt[:4000])
