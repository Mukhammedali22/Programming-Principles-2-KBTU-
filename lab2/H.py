import math
my_point = input().split()
n = int(input())
dict = {}
b = []
for i in range(n):
    coordinates = input()
    x, y = coordinates.split()
    distance = round(math.sqrt((int(x) - int(my_point[0])) ** 2 + (int(y) - int(my_point[1])) ** 2), 3)
    dict[coordinates] = distance
    b.append(distance)
a = list(dict.items())
b.sort()
for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j][1]:
            print(a[j][0])
