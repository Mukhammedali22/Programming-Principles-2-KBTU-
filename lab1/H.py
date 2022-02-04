s = input()
ch = input()
if s.count(ch) == 1:
    for i in range(len(s)):
        if s[i] == ch:
            print(i, end = ' ') 
            break
else:
    for i in range(len(s)):
        if s[i] == ch:
            print(i, end = ' ') 
            break
    for i in range(len(s) - 1, -1, -1):
        if(s[i] == ch):
            print(i)
            break
'''
s = input()            very short solution
ch = input()
print(s.find(ch)) if s.count(ch) == 1 else print(s.find(ch), s.rfind(ch))
'''