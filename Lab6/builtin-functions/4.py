import time
number = int(input("Sample Input:\n"))
milliseconds = int(input())
root = pow(number, 0.5) 
print("Sample Output:")
time.sleep(milliseconds / 1000)
print("Square root of", number, "after", milliseconds, "is", root)
