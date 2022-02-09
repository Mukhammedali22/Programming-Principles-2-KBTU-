n = int(input())
shelf = []
a = []
for i in range(n):
    x = input().split()
    if x[0] == "1":
        disc = x[1]
        shelf.append(disc)
    elif x[0] == "2":
        a.append(shelf[0])
        shelf.pop(0)
for i in a: print(i, end = " ")