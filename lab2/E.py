s = input().split()
if(len(s) == 1): b, a = int(input()), int(s[0])
else: a, b = int(s[0]), int(s[1])
arr = []
if a == 1: print(b)
else:
    for i in range(a):
        arr.append(b + 2 * i)
    x = arr[0] ^ arr[1]
    for i in range(a):
        if i == 0 or i == 1:
            continue       
        x ^= arr[i]
    print(x)
