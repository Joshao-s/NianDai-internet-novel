import json,os

Dict={}
for i in range(1,41):
    with open("data"+str(i)+".json", 'r', encoding="ANSI") as f:
        d = json.loads(f.read())
        Dict.update(d)
print(Dict)
json_str = json.dumps(Dict, indent=4)
with open('AllData.json', 'w',encoding='ANSI') as json_file:
    json_file.write(json_str)

os.system("del data*.json")