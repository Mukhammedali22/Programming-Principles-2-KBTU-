n = int(input())
a = []
c = set()
for i in range(n):
    upper, lower, number = False, False, False
    s = input()
    for j in s:
        if ord(j) >= 65 and ord(j) <= 90: upper = True
        elif ord(j) >= 97 and ord(j) <= 122: lower = True
        elif ord(j) >= 48 and ord(j) <= 57: number = True
    if upper == True and lower == True and number == True:
        c.add(s)
a = list(c)
a.sort()
print(len(a))
[print(i) for i in a]