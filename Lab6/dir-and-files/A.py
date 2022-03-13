for i in range(ord('A'), ord('Z') + 1):
    file = "{}.txt"
    f = open(file.format(chr(i)), "a")
    f.write("This file is not empty!")
f.close()