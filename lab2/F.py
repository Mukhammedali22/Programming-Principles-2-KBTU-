n = int(input())
dict = {}
c = set()
for i in range(n):
    student, money = input().split()
    c.add(student)
    if student in dict:
        dict[student] += int(money)
    else:
        dict[student] = int(money)
list_of_students = list(c)
list_of_students.sort()
m = max(dict.values())
for i in list_of_students:
    compensation = m - dict[i]
    if compensation == 0: print(i, "is lucky!")
    else: print(i, "has to receive", compensation, "tenge")
