def F_to_C(Fahrenheit):
    return (5 / 9) * (Fahrenheit - 32)
temperature = int(input())
print(F_to_C(temperature))