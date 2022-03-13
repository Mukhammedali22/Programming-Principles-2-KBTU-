a = open(r"C:\Users\Мухаммедали\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\kbtu\pp2\Lab5\The Little Prince.txt").read()
b = open("C:\\Users\\Мухаммедали\\OneDrive - АО Казахстанско-Британский Технический Университет\\Рабочий стол\\kbtu\\pp2\\Lab4\\json\\1.py").read()
c = open(r"C:\Users\Мухаммедали\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\kbtu\pp2\Lab5\The Little Prince.txt")
d = open("C:\\Users\\Мухаммедали\\OneDrive - АО Казахстанско-Британский Технический Университет\\Рабочий стол\\kbtu\\pp2\\Lab4\\json\\1.py")
e = open("D.txt").read()      # D.txt is empty file

if e:
    print(e.count("\n") + 1)  # if file is not empty 
else:
    print(e.count("\n"))      # if file is empty

print("first way with count() method where we count amount of lines in a file:")
print(a.count("\n") + 1)      # first way where we count amount of lines in a file with count() method
print(b.count("\n") + 1)

print("second way with readlines() which returns list of lines and we take its lenght as number of lines in a file:")
print(len(c.readlines()))     # second way with readlines() which returns list of lines and we take its lenght as number of lines in a file
print(len(d.readlines()))

# r"\a\b\c" or "\\a\\b\\c"    # как указывать пути в windows