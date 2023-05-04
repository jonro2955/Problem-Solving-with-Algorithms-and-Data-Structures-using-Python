# A function that takes a string and returns the reverse of it using recursion
def reverse(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[-1] + reverse(string[0:len(string)-1])


print(reverse("abcde"))


# A function that takes a string and returns True if it is a palindrome
def palindrome(string):
    return string == reverse(string)


print(palindrome('radar'))
