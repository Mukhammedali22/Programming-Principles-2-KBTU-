'''
def function(s):
    s = s.lower()
    print(s)
function(input())
'''

def function(s):
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90: print(chr(ord(i) + 32), end = "")
        else: print(i, end = "")
function(input())

'''
def to_lower(s):
    for i in range(len(s)):
        if s[i] >= 'A' and s[i] <= 'Z': print(chr(ord(s[i]) + 32), end = "")
        else: print(s[i], end = "")
to_lower(input())
'''