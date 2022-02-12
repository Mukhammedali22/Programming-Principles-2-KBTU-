def isPalindrome(my_word):
    reversed = my_word[::-1]
    print("Yes") if my_word == reversed else print("No")
isPalindrome(input())