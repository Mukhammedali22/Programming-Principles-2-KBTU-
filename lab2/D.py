n = int(input())
a = []
b = []
[a.append(i) for i in range(n)]
[b.append(i) for i in range(n)]
if n % 2 == 1:
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1: print("#", end = "")
            else: print(".", end = "")
        print()
else:
    for i in range(n):
        for j in range(n):
            if i >= j: print("#", end = "")
            else: print(".", end = "")
        print()
