import datetime
x = datetime.datetime.now()
# first way
date_without_microseconds = x.replace(microsecond = 0)
print(date_without_microseconds)

# second way
a = datetime.datetime.strftime(x, "%Y-%m-%d %H:%M:%S")
print(a)