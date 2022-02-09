import math
my_point = input().split()
n = int(input())
dict = {}
b = []
for i in range(n):
    coordinates = input()
    a = coordinates.split()
    distance = round(math.sqrt((int(a[0]) - int(my_point[0])) ** 2 + (int(a[1]) - int(my_point[1])) ** 2), 3)
    dict[coordinates] = distance
    b.append(distance)
x = list(dict.items())
b.sort()
for i in range(len(b)):
    for j in range(len(x)):
        if b[i] == x[j][1]:
            print(x[j][0])
