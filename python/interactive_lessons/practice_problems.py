# Python Lesson 8.2 - Practice Problems

# Define a function is_even that will take a number x as input. If x is even then return True. Otherwise, return False.
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

# print is_even(2.0)
# print is_even(3)


# Define a function is_int that takes a number x as an input. Have it return True if the numbers is an interger (a number without a decimal part or with a decimal part that is all 0s) and False otherwise.
def is_int(x):
    if x == int(x):
        return True
    else:
        return False

# print is_int(7.0)
# print is_int(7.5)
# print is_int(-1)

# def is_int(x):
#     absoluteCount = abs(x)
#     typeCount = type(x)
#     roundCount = round(absoluteCount)
#     if typeCount and absoluteCount - roundCount == 0:
#         return True
#     else:
#         return False


# Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits. For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. Assume the number you are given will always be positive.
def digit_sum(n):
    stringify = str(n)
    result = 0
    for digit in stringify:
        result += int(digit)
    return result

# print digit_sum(1234)


# Define a function factorial that takes an integer x as input. Calculate and return the factorial of that number.
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

# print factorial(4)
# print factorial(1)
# print factorial(3)

# def factorial(x):
#     total = 1
#     while x > 0:
#         totral *= x
#         x-= 1
#     return total


# Define a function called is_prime that takes a number x as input. For each number n from 2 to x -1, test if x is evenly divisible by n. If it is, return False. If none of them are, then return True.
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True

# print is_prime(2)
# print is_prime(11)
# print is_prime(18)


# Define a function called reverse that takes a string text and returns that string in reerse. For example: reverse("abcd") should return "dcba". You may not use reversed or [::-1] to help you with this. You may get a string containing special characters (for example, !, @, or #).
def reverse(text):
    reversed_letters = " "
    while len(text) > 0:
        reversed_letters += text[-1]
        text = text[:-1]
    return reversed_letters

# print reverse("abcd")
# print reverse("Python!")


# Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed. Don't count Y as a vowel. Make sure to remove lowercase and uppercase vowels
def anti_vowel(text):
    vowelless = ""
    for c in text:
        if c not in "aeiouAEIOU":
            vowelless += c
    return vowelless

print anti_vowel("Hey You!")