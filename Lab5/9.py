import re
txt = "YouArePrettiesteGirlIHaveEverSeen, perfectNumber, BinToDec, camelCase, UpperCase"
x = re.findall("[A-Z][a-z]*", txt)
for i in x:
    print(i, end = " ")
