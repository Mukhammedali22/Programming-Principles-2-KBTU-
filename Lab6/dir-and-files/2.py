import os
path = r"C:\Users\Мухаммедали\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\kbtu\pp2\Lab5\The Little Prince.txt"
f = open(path)
if os.path.exists(path):
    print("YES, the path is exist!")
else:
    print("does not exist :(")
print(f.readable())
print(f.writable()) # доступен просмотр
if os.access(path, os.X_OK):
    print("YES, it's executable!")
else:
    print("NO")