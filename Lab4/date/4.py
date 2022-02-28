import datetime
first_date = input()
second_date = input()
a = datetime.datetime.strptime(first_date, "%Y-%m-%d %H:%M:%S")
b = datetime.datetime.strptime(second_date, "%Y-%m-%d %H:%M:%S")
difference = abs(a - b) 
print(difference.days * 24 * 60 * 60 + difference.seconds, "seconds")