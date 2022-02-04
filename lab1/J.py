s = input().split()
#for x in s:
#    if(len(x) >= 3): print(x, end = ' ')

[print(x, end = " ") for x in s if len(x) >= 3]