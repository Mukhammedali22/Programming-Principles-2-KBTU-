n = int(input())
ch = input()
if ch == "k":
    x = int(input()) 
    print(round(n / 1024, x))
elif ch == "b": print(n * 1024)