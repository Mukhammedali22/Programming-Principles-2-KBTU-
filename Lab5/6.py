import re
txt = open("The Little Prince.txt").read()
x = re.sub('[ ,.]', ':', txt)
print("before", txt)
print("after", x)