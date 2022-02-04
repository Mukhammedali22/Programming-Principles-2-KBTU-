'''
for i in range(int(input())):
    s = input()
    if s.find("@gmail.com") != -1: #print(s.replace("@gmail.com", ""))
        s = s.replace("gmail.com", "")
        print(s)
'''

for i in range(int(input())):
    s = input() 
    #if s.find("@gmail.com") != -1: print(s.replace("@gmail.com", ""))
    #if "@gmail.com" in s: print(s.replace("@gmail.com", ""))
    if "@gmail.com" in s: print(s[:-10])