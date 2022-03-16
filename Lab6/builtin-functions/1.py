my_list = [i for i in range(1, 10)]
product = 1
for i in range(len(my_list)):
    product *= my_list[i]
print(product)

''' 
import math                                # second way
a = [i for i in range(1, 10)]
product = math.prod(a)
print(product)
'''
