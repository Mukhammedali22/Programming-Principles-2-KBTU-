my_list = [i for i in range(1, 10)]
if all(my_list):
    product = 1
    for i in my_list:
        product *= i
    print(sum)
else:
    print("NO")
