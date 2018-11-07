# Python Lesson 3.2 - Conditionals & Control Flow

print "Welcome to the Pig Latin Translator!"

# raw_input takes in user input
original = raw_input("Please enter a word: ")

# Create variable for suffix
pyg = "ay" 

# If statement to ensure user input a non-numeric word
if len(original) > 0 and original.isalpha():
    #Convert input to lower case
    word = original.lower()
    #Variable to hold first letter of word
    first = word[0]
    #Concatenating word + first + pyg together for translation into new variable
    new_word = word + first + pyg
    #Returning new word without repeat of first letter in original & new position by slicing
    new_word = new_word[1:len(new_word)]
    print original + " in Pig Latin is " + new_word
else:
    print "Your input is invalid :("