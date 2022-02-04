'''
s = input()                           without recursion
to_decimal = 0
power = 1
for i in range(len(s) - 1, -1, -1):
    to_decimal += int(s[i]) * power
    power *= 2
print(to_decimal)
'''

def to_decimal(s, i):
    decimal = 0
    if i == len(s):
        return decimal
    else:
        decimal = int(s[len(s) - 1 - i]) * 2 ** i
        return decimal + to_decimal(s, i + 1)

s = input()
print(to_decimal(s, 0))