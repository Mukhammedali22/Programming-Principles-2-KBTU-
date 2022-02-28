my_number = int(input())
def my_generator(my_number):
    for i in range(my_number):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for i in my_generator(my_number):
    print(i)