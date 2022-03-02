import json
with open("sample-data.json") as jsonFile:
    x = json.load(jsonFile)
print(
"""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
"""
)
for i in x["imdata"]:
    print('{DN:50}{Speed:>29}{MTU:>7}'.format(DN = i["l1PhysIf"]["attributes"]["dn"], Speed = i["l1PhysIf"]["attributes"]["speed"], MTU = i["l1PhysIf"]["attributes"]["mtu"]))
    # удлиняем нашу строку до заданной длины добавляя ей пробелов, а затем печатаем получившую новую строку
