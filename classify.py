import json
Dict={}
with open("AllData.json", 'r', encoding="ANSI") as f:
    Dict = json.loads(f.read())
D={}
for i in range(2012,2022):
    D[i]={}
for a in Dict:
    year=int(Dict[a]['year'])
    D[year][a]=Dict[a]
for i in range(2012,2022):
    print(i,len(D[i]))
    json_str = json.dumps(D[i], indent=4)
    with open('AllData'+str(i)+'.json', 'w',encoding='ANSI') as json_file:
        json_file.write(json_str)
print("total", len(Dict))