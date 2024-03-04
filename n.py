import json

with open("j.json",'r') as file:
    js = json.load(file)

zero = js['items'][0]

with open("data.json",'w') as file:
    json.dump(zero,file,indent= 4 )

