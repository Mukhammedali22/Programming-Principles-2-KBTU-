import re
txt = open("The Little Prince.txt").read()
x = re.findall('ab{2,3}', txt)
if x: print(x)
else: print("there is no such string in the text")