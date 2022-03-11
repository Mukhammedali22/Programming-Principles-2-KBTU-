import re
txt = open("The Little Prince.txt").read()
x = re.split("[A-Z]+[a-z]*", txt)
print(x)