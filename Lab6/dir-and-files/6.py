for i in range(ord('A'), ord('Z') + 1):
    file = "{}.txt"
    f = open(file.format(chr(i)), "x")