dish = input()
sum = 0
for x in dish:
    sum += ord(x)
print("It is tasty!") if sum > 300 else print("Oh, no!")