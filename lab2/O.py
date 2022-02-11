def my_calculator(my_list):
    dict = {
        "ZER": "0",
        "ONE": "1",
        "TWO": "2",
        "THR": "3",
        "FOU": "4",
        "FIV": "5",
        "SIX": "6",
        "SEV": "7",
        "EIG": "8",
        "NIN": "9",
    }
    my_list = my_list.split('+')
    keys = list(dict.keys())
    c = []
    for i in my_list:
        a = []
        for j in range(0, len(i), 3):
            a.append(i[j: j + 3])
        c.append(a)
    sum = int()
    for i in c:
        number = int()
        for j in range(len(i)):
            for k in keys:
                if i[j] == k:
                    number += int(dict[k]) * 10 ** (len(i) - 1 - j)
        sum += number
    my_sum = str()
    for i in str(sum):
        for j in keys:
            if dict[j] == i: my_sum += j
    print(my_sum)

s = input()
my_calculator(s)