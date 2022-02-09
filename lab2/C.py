n = int(input())
a = []
b = []
for i in range(n):
    a.append(i)
    b.append(i)
for i in range(n):
    for j in range(n):
        if i == 0: print(b[j], end = " ")
        elif j == 0: print(a[i], end = " ")
        elif j == i: print(a[i] * b[i], end = " ")
        else: print(0, end = " ")
    print()