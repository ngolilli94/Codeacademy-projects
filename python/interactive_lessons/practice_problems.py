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

# print anti_vowel("Hey You!")


# Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word. Assume you input is only one word contaning no spaces or punctuation. Your function should work even if the letters you get are uppercase, lowercase, or a mix. Assume that you're only given non-empty strings.
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
    case_insensitive = word.lower()
    word_score = 0
    for letter in case_insensitive:
        word_score += score[letter]
    return word_score

# print scrabble_score("Helix")


# Write a function called censor that takes two strings, text and word, as input. It should return the text with the word you chose replaced with asterisks. Assume you input strings won't contain punctuation or upper case letters. The number of asterisks you put should correspond to the number of letters in the censored word.
def censor(text, word):
    split_text = text.split()
    censored_text = []
    for i in split_text:
        if i == word:
            i = "*" * len(word)
        censored_text.append(i)
    return " ".join(censored_text)

# print censor("this hack is wack hack", "hack")


# Define a function callled count that has two arguments called sequence and item. Return the number of times the item occurs in the list. For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).
def count(sequence, item):
    tally = 0
    for i in sequence:
        if i == item:
            tally += 1
    return tally

# print count([1, 2, 1, 1], 1)


# Define a function called purify that takes in a list of numbers, removes all odd numbers in the list and returns the result. For example, purify([1, 2, 3]) should return [2]. Do not directly modify the list you are given as input; instead, return a new list with only the even nnumbers.
def purify(lst):
    even_only = []
    for num in lst:
        if num % 2 == 0:
            even_only.append(num)
    return even_only

# print purify([1, 2, 3])
# print purify([-4, -3, -1, 0, 2, 2.2])


# Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list. For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100). Don't worry about the list being empty. Your function should return an integer.
def product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# print product([4, 5, 5])
# print product([-2, 1, 10])
# print product([2.5, 4, 10])


# Define a function remove_duplicates that takes in a list and removes elements of the list that are the same. For exmaple: remove_duplicates([1, 1, 2, 2]) should return [1, 2].
def remove_duplicates(lst):
    single_occurence = []
    for ele in lst:
        if ele not in single_occurence:
            single_occurence.append(ele)
    return single_occurence

# print remove_duplicates([1, 1, 2, 2])
# print remove_duplicates([-2, -2, 1, 2, 2.0])


# Write a function called median that takes a list as an input and returns the median value of the lst. For example: median([1, 1, 2]) should return 1. The list can be of any size; if the list contains an even number of elements, your function should return the average of the middle two.
def median(lst):
    ordered_list = sorted(lst)
    midway = len(ordered_list) / 2
    if len(ordered_list) % 2 == 0:
        mid_two = ordered_list[midway] + ordered_list[midway -1]
        return mid_two / 2.0
    else:
        return ordered_list[(len(ordered_list) - 1) / 2]

# print median([7, 12, 3, 1, 6])
# print median([7, 3, 1, 4])