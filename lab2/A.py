s = input().split()
a = len(s) - 1
for i in range(len(s) - 2, -1, -1): 
    if i + int(s[i]) >= a: a = i 
print("1") if a == 0 else print("0")