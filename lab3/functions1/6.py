def my_function(string):
    string = string.split()
    string.sort(reverse = True)
    for i in string:
        print(i, end = " ")
my_function(input())
