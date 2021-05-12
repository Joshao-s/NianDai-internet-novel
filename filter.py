import re,json

wen="零一二三四五六七八九"
map1={}
for i in range(0,10):
    map1[wen[i]+"零"]=i
map2={}
for i in range(0,10):
    map2[wen[i]+"十"]=i

year=int(input())
if year>=2012 and year<=2021:
    Dict={}
    with open("AllData"+str(year)+".json", 'r', encoding="ANSI") as f:
        Dict = json.loads(f.read())
    print("total",len(Dict))
    Counter={}

    for i in range(10):
        Counter[i]=0
    
    for a in Dict:
        name=a
        Into=Dict[a]['into']
        flag=0
        # x零 作为关键词
        for tag in map1:
            if tag in name or tag in Into:
                ii=map1[tag]
                Counter[ii]=Counter[ii]+1
                flag=1
                break
        if flag==1:
            continue
        # x十 作为关键词
        for tag in map2:
            if tag in name or tag in Into:
                ii=map2[tag]
                Counter[ii]=Counter[ii]+1
                flag=1
                break
        if flag==1:
            continue
        # 数字 作为关键词
        NameNumber= re.findall("\d+",name)
        if len(NameNumber)>=1:
            NameNumber= int(NameNumber[0])
            if NameNumber>10 and NameNumber<100:
                ii=NameNumber//10
                Counter[ii]=Counter[ii]+1
                flag=1
            elif NameNumber>1910 and NameNumber<2000:
                ii=(NameNumber-1900)//10
                Counter[ii]=Counter[ii]+1
                flag=1
        if flag==1:
            continue
        IntoNumber= re.findall("\d+",Into)
        if len(IntoNumber)>=1:
            IntoNumber= int(IntoNumber[0])
            if IntoNumber>10 and IntoNumber<100:
                ii=IntoNumber//10
                Counter[ii]=Counter[ii]+1
                flag=1
            elif IntoNumber>1910 and IntoNumber<2000:
                ii=(IntoNumber-1900)//10
                Counter[ii]=Counter[ii]+1
                flag=1
        if flag==1:
            
            continue
        print(a,Dict[a])
    
    print("total",len(Dict))
    for i in range(10):
        print(str(i)+'0年代',Counter[i])