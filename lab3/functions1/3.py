def solve(numheads, numlegs):
    rabbits = int(numlegs) // 2 - int(numheads)
    chickens = int(numheads) - rabbits
    print("rabbits:", rabbits, "chickens:", chickens)
heads, legs = input().split()
solve(heads, legs)