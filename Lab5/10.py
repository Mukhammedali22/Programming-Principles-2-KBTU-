import re
txt =  "myName perfectNumber, snakeCase, upperCase, binToDec, aliZak"  #camel case
x = re.findall("[a-z]+[A-Z]+[a-z]+", txt)
print(x)
for i in x:
    f, s = "", ""
    for j in i:
        if j >= 'a' and j <= 'z': f += j
        else: break
        s = i.replace(f, "")
    print(f + '_' + s.lower(), end = " ")