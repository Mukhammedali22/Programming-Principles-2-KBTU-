def filter_prime(my_list):

    def prime(number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    for i in my_list:
        if prime(int(i)):
            print(i, end = " ")

numbers = input().split()
filter_prime(numbers)