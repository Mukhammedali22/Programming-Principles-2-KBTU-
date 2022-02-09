n = int(input())
a = input().split()
c = set({})
for i in range(n):
    for j in range(n):
        if i != j: 
            c.add(int(a[i]) * int(a[j]))
print(max(c))

'''
n = int(input())              
a = input().split()
b = []
[b.append(int(a[i])) for i in range(n)]
b.sort()
print(int(b[-1]) * int(b[-2]))
'''