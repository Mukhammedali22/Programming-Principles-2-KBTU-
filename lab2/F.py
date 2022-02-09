n = int(input())
dict = {}
for i in range(n):
    student, money = input().split()
    if student in dict:
        dict[student] += int(money)
    else:
        dict[student] = int(money)
list_of_students = list(dict.keys())
list_of_students.sort()
m = max(dict.values())
for i in list_of_students:
    compensation = m - dict[i]
    if compensation == 0: print(i, "is lucky!")
    else: print(i, "has to receive", compensation, "tenge")
