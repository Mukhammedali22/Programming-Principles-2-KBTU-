def prime(n):
    for i in range(2, n):
        if n % i == 0: 
            return False 
    return True
s = input().split()
distance = int(s[0])
patrony = int(s[1])
if distance <= 500 and prime(distance): print("Good job!") if patrony % 2 == 0 else print("Try next time!")
else: print("Try next time!")
    
'''
def prime(n):
    for i in range(2, n):
        if n % i == 0: return False 
    return True
s = input().split()
print("Good job!") if int(s[0]) <= 500 and prime(int(s[0])) and int(s[1]) % 2 == 0 else print("Try next time!")
'''
