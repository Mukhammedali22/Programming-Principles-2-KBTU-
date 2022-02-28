my_number = int(input())
def my_generator(my_number):
    for i in range(0, my_number, 2):
        if i + 2 == my_number:
            print(str(i))
        else:
            print(str(i) + ',', end = " ")
my_generator(my_number)