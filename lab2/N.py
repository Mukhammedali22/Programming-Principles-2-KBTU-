a = []
n = int(input())
a.append(n)
i = 0
while a[i] != 0:
    m = int(input())
    if m == 0: break
    a.append(m)
    i += 1
if len(a) % 2 == 0:
    for i in range(len(a) // 2):
        print(a[i] + a[-1 - i], end = " ")
else:
    for i in range(len(a) // 2):
        print(a[i] + a[-1 - i], end = " ")
        if i + 1 == len(a) // 2: print(a[i + 1], end = " ")
