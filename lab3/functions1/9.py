import math
def volume_of_sphere(radius):
    V = (4 / 3) * math.pi * radius ** 3
    return V
radius = int(input())
print(volume_of_sphere(radius))