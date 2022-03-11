import re
txt = open("The Little Prince.txt").read()
#print(txt)
x = re.findall('ab*', txt)
print(x)