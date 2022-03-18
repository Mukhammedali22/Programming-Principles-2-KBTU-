import os
root = r"C:\Users\Мухаммедали\OneDrive - АО Казахстанско-Британский Технический Университет\Рабочий стол\kbtu\pp1"

#subdirs = [i[0] for i in os.walk(path)]
#print(subdirs)

#print("list of only directories\n")
directory = open("directory.txt", "x")
directory.write("list of only directories:\n")
for path, subdirs, files in os.walk(root):
    for name in subdirs:
        directory.write(name + "\n")
directory.close()
        #print(os.path.join(path, name))
        #print(name)
#print("\nlist of only files:\n")
file = open("files.txt", "x")
file.write("list of only files:\n")
for path, subdirs, files in os.walk(root):
    for name in files:
        #print(os.path.join(path, name))
        #print(name)
        file.write(name + "\n")
file.close()
#print("\nlist of all directories and files:\n")
all = open("all.txt", "x", encoding = "utf-8")
all.write("list of all directories and files:\n")
for path, subdirs, files in os.walk(root):
    for name in files:
        #print(os.path.join(path, name))
        all.write(os.path.join(path, name) + "\n")
all.close()
