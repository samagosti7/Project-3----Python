"""Initial Comment
X for placed battleship and hit battleship
' ' for available
"-" for miss """

from random import randint

print("Hello")
COMPUTER_BOARD = [[" "]*7 for x in range(7)]
GUESS_BOARD = [[" "]*7 for x in range(7)]


letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}


def print_board(board):
    print("  A B C D E F G")
    print("  -------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    for ship in range(4):
        ship_row, ship_column = randint(0, 6), randint(0, 6)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 6), randint(0, 6)
        board[ship_row][ship_column] = "X"

def get_ship_location():
    row = input("Enter ship row between 1 and 7:  \n")
    column = input("Enter ship column between A-G:  \n").upper()
    return int(row)-1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


create_ships(COMPUTER_BOARD)
turns = 18
print_board(COMPUTER_BOARD)
print("Ahoy admiral, prepare for war! We have 18 shots for the heavy artillery and reconnaissance tells us there are 4 enemy ships lurking in the area. A blank map of the sea is below, and the gunners are standing by--so it's up to you to find the enemy!")
while turns > 0:
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == "-":
        print("Uh...you already guessed that. Are you ok admiral?")
    elif COMPUTER_BOARD[row][column] == "X":
        print("A hit! Well shot, sir, ship sunk.")
        GUESS_BOARD[row][column] = "X"
        turns -= 1
    else:
        print("No luck sir, shot missed.")
        GUESS_BOARD[row][column] = "-"
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 4:
        print("That's the last of them sir, we've done it! All battleships sunk, we've won!")
        break
    print(f"You have {turns} turns left.")
    if turns == 0:
        print("We're out of time. We ran out of turns, so the enemy has escaped with their remaining vessels.")