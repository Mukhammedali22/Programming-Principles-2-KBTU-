import re
txt = open("The Little Prince.txt").read()
x = re.findall("[A-Z]+[a-z]*", txt)
for i in x:
    print(i, end = " ")