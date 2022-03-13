import re
txt = "YouArePrettiesteGirlIHaveEverSeen, perfectNumber, BinToDec, camelCase, UpperCase"
x = re.sub(r"([A-Z][a-z]*)([A-Z][a-z]*)", r"\1 \2 ", txt).strip()
x = re.sub(r"( ,)+", r",", x)
print(x)

'''
import re
txt = "YouArePrettiesteGirlIHaveEverSeen, perfectNumber, BinToDec, camelCase, UpperCase"
x = re.findall("[A-Z][a-z]*", txt)
for i in x:
    print(i, end = " ")
'''
