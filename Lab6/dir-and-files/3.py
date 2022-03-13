import os
path = "C:\\Users\\Мухаммедали\\OneDrive - АО Казахстанско-Британский Технический Университет\\Рабочий стол\\kbtu\\pp2\\Lab5\\The Little Prince.txt"
if os.path.exists(path):
    fileName = os.path.basename(path)
    path_to_file = os.path.dirname(path)
    print(fileName)
    print(path_to_file)
else:
    print("The path does not exist")