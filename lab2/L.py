a = input()
b = []
for i in a:
    if i == '{' or i == '[' or i == '(': b.append(i)
    else:
        if(len(b) != 0):
            if b[-1] == '{' and i == '}': b.pop()
            elif b[-1] == '[' and i == ']': b.pop()
            elif b[-1] == '(' and i == ')': b.pop()
        else:
            print("No")
            break
else: print("Yes") if len(b) == 0 else print("No")