def histogram(my_list):
    for i in my_list:
        for j in range(int(i)):
            print("*", end = "")
        print()
histogram(input().split())