s = input()
upper, lower = 0, 0
for i in range(len(s)):
    if ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z'):
        upper += 1
    elif ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z'):
        lower += 1
print("number of upper case letters:", upper, "\nnumber of lower case letters:", lower)