import requests
from bs4 import BeautifulSoup
from CMdiagnose.models import Cases

for i in range(601, 9271):
    page = requests.get("http://yibian.hopto.org/wang/?wno=" + str(i), proxies={'http': 'proxy5.edb.gov.hk:8080'},timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    n=str(soup)[int(str(soup).find("方名")):]
    name_=n[int(n.find("方名</td>\n<th align=\"left\" nowrap=\"\">")): int(n.find("</th>"))].replace('方名</td>\n<th align=\"left\" nowrap=\"\">','')
    zf=str(soup)[int(str(soup).find("【製法用量】")): int(str(soup).find("【功效】"))]
    zf=zf[int(zf.find("【製法用量】")): int(zf.find("。<p>"))].replace('<p>','')
    x=str(soup)[int(str(soup).find("【功效】")): int(str(soup).find("【主治】"))]
    x=x[int(x.find("【功效】")): int(x.find(">【"))].replace('<p>','').replace('<p','')
    zz=str(soup)[int(str(soup).find("【主治】")): ]
    zz=zz.replace(zz[int(zz.find("<table")):],'')
    fy=str(soup)[int(str(soup).find("【方義】")): ]
    fy=fy.replace(fy[int(fy.find("<table")):],'')
    fy=fy.replace(fy[int(fy.find("<center>")):],'')
    xd=str(soup)[int(str(soup).find("【現代應用】")):]
    xd=xd.replace(xd[int(xd.find("<center>")):],'')
    xd=xd.replace(xd[int(xd.find("<table")):],'')
    smpt=x+zz
    fcts=smpt.replace('【功效】','').replace('【主治】','').replace('者','').replace('，',',').replace('。',',').replace('、',',').replace('<p>','')
    y=Cases(solution=name_+" "+zf, facts=fcts, symptom=smpt, reference=fy+xd)
    y.save()
    print(str(i) + " finished")