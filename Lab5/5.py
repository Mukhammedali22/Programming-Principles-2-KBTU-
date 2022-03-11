import re
txt = open("The Little Prince.txt").read()
x = re.findall("^a.*b$", txt)
if x: print("YES", x)
else: print("NO")