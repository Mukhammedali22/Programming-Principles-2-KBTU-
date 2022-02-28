a, b = map(int, input().split())
def squares():
    for i in range(b):
        if i * i >= a and i * i <= b:
            yield i * i

for i in squares():
    print(i)