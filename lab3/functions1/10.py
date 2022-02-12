from ast import Pass


def unique(my_list):
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    print(new_list)
unique(input().split())
