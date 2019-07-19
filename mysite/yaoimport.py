import requests
from bs4 import BeautifulSoup
from CMdiagnose.models import Yao

# for i in range(51, 101):
#     page = requests.get("http://yibian.hopto.org/yao/?yno=" + str(i),timeout=5)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     n=str(soup)[int(str(soup).find("藥名")):]
#     name_=n[int(n.find("<b>")): int(n.find("</b>"))].replace('<b>','')
#     xw=str(soup)[int(str(soup).find("【性味歸經】")): int(str(soup).find("【功效】"))]
#     xw=xw[int(xw.find("【性味歸經】")): int(xw.find("。<p>"))].replace('<p>','')
#     x=str(soup)[int(str(soup).find("【功效】")): int(str(soup).find("【主治】"))]
#     x=x[int(x.find("【功效】")): int(x.find("。<p>"))].replace('<p>','')
#     zz=str(soup)[int(str(soup).find("【主治】")): int(str(soup).find("【文獻別錄】"))]
#     zz=zz[int(zz.find("【主治】")): int(zz.find("。<p>"))].replace('<p>','')
#     zz=zz[int(zz.find("【主治】")): ].replace(zz[int(zz.find("</li></li></li></li></ol>\n\n")):],'')
#     jj=str(soup)[int(str(soup).find("【注意禁忌】")): int(str(soup).find("【現代藥理】"))]
#     jj=jj[int(jj.find("【注意禁忌】")): int(jj.find("。<p>"))].replace('<p>','')
#     jj=jj[int(jj.find("【注意禁忌】")): ].replace(jj[int(jj.find("</li></li></li></li></ol>\n\n")):],'')
#     xd=str(soup)[int(str(soup).find("【現代藥理】")):]
#     xd=xd[int(xd.find("【現代藥理】")): int(xd.find("。<p>"))].replace('<p>','')
#     xd=xd[int(xd.find("【現代藥理】")): ].replace(xd[int(xd.find("</li></li></li></li></ol>\n\n")):],'')
#     y=Yao(name=name_, responses=xw+x, properties=zz+jj+xd)
#     y.save()

for i in range(1, 51):
    page = requests.get("http://yibian.hopto.org/yao/?yno=" + str(i), proxies={'http': 'proxy5.edb.gov.hk:8080'},timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    n=str(soup)[int(str(soup).find("藥名")):]
    name_=n[int(n.find("<b>")): int(n.find("</b>"))].replace('<b>','')
    xw=str(soup)[int(str(soup).find("【性味歸經】")): int(str(soup).find("【功效】"))]
    xw=xw[int(xw.find("【性味歸經】")): int(xw.find("。<p>"))].replace('<p>','')
    x=str(soup)[int(str(soup).find("【功效】")): int(str(soup).find("【主治】"))]
    x=x[int(x.find("【功效】")): int(x.find("。<p>"))].replace('<p>','')
    zz=str(soup)[int(str(soup).find("【主治】")): int(str(soup).find("【文獻別錄】"))]
    zz=zz[int(zz.find("【主治】")): int(zz.find("。<p>"))].replace('<p>','')
    jj=str(soup)[int(str(soup).find("【注意禁忌】")): int(str(soup).find("【現代藥理】"))]
    jj=jj[int(jj.find("【注意禁忌】")): int(jj.find("。<p>"))].replace('<p>','')
    xd=str(soup)[int(str(soup).find("【現代藥理】")):]
    xd=xd[int(xd.find("【現代藥理】")): int(xd.find("。<p>"))].replace('<p>','')
    y=Yao(name=name_, responses=xw+x, properties=zz+jj+xd)
    y.save()

    