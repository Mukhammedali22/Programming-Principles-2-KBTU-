s = input()
a = reversed(s)
r = "".join(a)
print("YES") if s == r else print("NO")