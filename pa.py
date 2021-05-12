import requests,re,json
from bs4 import BeautifulSoup
from collections import defaultdict, OrderedDict

rule1=r'>(.*?)<'
rule2=r'：(.*?)\n'
rule3=r'>(.*?)-'
for j in range(1,41):
    d={}
    url = 'http://www.jjwxc.net/bookbase.php?fw=0&ycx=0&xx=0&mainview=0&sd=0&lx=0&fg=0&bq=173&sortType=3&isfinish=0&collectiontypes=&searchkeywords=&page='+str(j)
    r = requests.get(url)
    r.encoding = 'ANSI'
    html = r.text
    soup = BeautifulSoup(html, "lxml")
    # 列数处理
    ll=102
    if j==41:
        ll=87
    # 开始解析
    for i in range(2,ll):
        print(i,j)
        data=soup.select('body > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(6)')
        data=str(data)
        number=re.findall(rule1, data)
        #根据字数进行筛选
        if int(number[0])<100000:
            continue
        data=soup.select('body > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(2) > a')
        data=str(data)
        name=re.findall(rule1, data)
        d[name[0]]={}
        d[name[0]]['number']=number[0]

        into=re.findall(rule2, data)
        d[name[0]]['into']=into[0]

        data=soup.select('body > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(8)')
        data=str(data)
        year=re.findall(rule3, data)
        d[name[0]]['year']=year[0]
    json_str = json.dumps(d, indent=4)
    with open('data'+str(j)+'.json', 'w',encoding='ANSI') as json_file:
        json_file.write(json_str)
