import re
txt = "YouArePrettiestGirlIHaveEverSeen"
x = re.sub(r"([A-Z][a-z]*)([A-Z][a-z]*)", r"\1 \2 ", txt).strip()
print(x)

'''
import re
txt = "YouArePrettiestGirlIHaveEverSeen"
x = re.findall("[A-Z][a-z]*", txt)
for i in x:
    print(i, end = " ")
'''
