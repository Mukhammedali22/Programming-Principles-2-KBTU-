def my_function(date):
    date = date.split()
    return int(date[2]), int(date[1]), int(date[0])
a  = input()
dates = [a]
while a != "0":
    a = input()
    if a != "0":
        dates.append(a)
dates.sort(key = my_function)
[print(i) for i in dates]