#a = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
#a = [str(i) for i in range(10)]
#a = [chr(i) for i in range(ord('a'), ord('z') + 1)]
a = open(r"C:\Users\Мухаммедали\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\kbtu\pp2\Lab5\The Little Prince.txt").readlines()
f = open("C.txt", "a")
for i in a:
    f.write(i)
f.write("\n")
f.close()
f = open("C.txt").read()
print(f)