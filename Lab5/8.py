import re
txt = "YouArePrettiestGirlIHaveEverSeen"
x = re.findall("[A-Z][a-z]*", txt)
for i in x:
    print(i, end = " ")
