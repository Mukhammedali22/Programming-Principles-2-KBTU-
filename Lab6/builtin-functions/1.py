my_list = [i for i in range(1, 10)]
if all(my_list):
    product = 1
    for i in my_list:
        product *= i
    print(sum)
else:
    print("NO")

'''  
import math                                # second way
a = [i for i in range(1, 10)]
if all(a):
    product = math.prod(a)
    print(product)
else:
    print("Not iterable")
'''
