def solve(numheads, numlegs):
    if int(numlegs) % 2 != 0: 
        print("Error. Number of legs is odd")
    else:
        rabbits = int(numlegs) // 2 - int(numheads)
        chickens = int(numheads) - rabbits
        if rabbits >= 0 and chickens >= 0 and rabbits + chickens == int(numheads):
            print("rabbits:", rabbits, "chickens:", chickens)
        else:
            print("No solution")
heads, legs = input().split()
solve(heads, legs)
