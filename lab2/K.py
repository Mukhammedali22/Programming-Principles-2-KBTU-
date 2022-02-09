s = input().split()
a = []
c = set()
for i in s:
    for j in i:
        if ord(j) < 65 or (ord(j) > 90 and ord(j) < 97) or ord(j) > 122:
            i = i.replace(j, "")
    c.add(i)
a = list(c)
a.sort()
print(len(a))
for i in a: print(i)