my_number = int(input())
def generator(my_number):
    while(my_number > -1):
        yield my_number
        my_number -= 1
for i in generator(my_number):
    print(i)