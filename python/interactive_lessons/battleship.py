# Python Lesson 7.2 - Lists & Functions
from random import randint

board = []

# print ["O"] * 5
# Looping through range to create 5x5 board
for i in range(5):
    board.append(["O"] * 5)

# Printing board as grid
def print_board(board_in):
    for row in board:
        # .join() to print w/o quotes, commas, & brackets
        print " ".join(row)
 
# Hiding battlehship in random location on board using random module
def random_row(board_in):
    return randint(0, len(board_in) - 1)

def random_col(board_in):
    return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Printing ship location for mod purposes
print ship_row
print ship_col

# Allowing user 4 turns
for turn in range(4):
    print "Turn " + str(turn + 1)
    # Allowing user to guess ship location 
    guess_row = int(raw_input("Guess a row: "))
    guess_col = int(raw_input("Guess a column: "))
    # Checking if user guess is correct & if so, break out of loop
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        break 
    else:
        # If statement to check if user guess within range of board
        if guess_row not in range(5) or guess_col not in range(5):
            print "Oops, that's not even in the ocean!"
        # Check if location had been previously guessed already
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already"
        else:
            # Indicate guessed location
            board[guess_row][guess_col] = "X"
            print "You missed my battleship! Try again!"
            print_board(board)
# Let user know if out of guesses
if turn == 3:
    print "Looks like you're out of ammo--Game Over"


# print_board(board)
