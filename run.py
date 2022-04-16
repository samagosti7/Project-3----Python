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

def hide_ships():
    # Ship One
    print("Time to position our first ship")
    ship_one_row = input("Enter ship row between 1-7 \n")
    while ship_one_row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Incorrect input")
        ship_one_row = input("Enter ship row between 1-7 \n")
    ship_one_column = input("Enter ship column between A-G \n").upper()
    while ship_one_column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Incorrect input")
        ship_one_column = input("Enter ship column between A-G \n").upper()
    ship_one_position = (int(ship_one_row)-1, letters_to_numbers[ship_one_column])
    print("Ship one in position")
    # Ship Two
    print("Time to position our second ship")
    ship_two_row = input("Enter ship row between 1-7 \n")
    while ship_one_row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Incorrect input")
        ship_two_row = input("Enter ship row between 1-7 \n")
    ship_two_column = input("Enter ship column between A-G \n").upper()
    while ship_one_column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Incorrect input")
        ship_two_column = input("Enter ship column between A-G \n").upper()
    ship_two_position = (int(ship_two_row)-1, letters_to_numbers[ship_two_column])
    print("Ship two in position")
    # Ship Three
    print("Time to position our third ship")
    ship_three_row = input("Enter ship row between 1-7 \n")
    while ship_three_row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Incorrect input")
        ship_three_row = input("Enter ship row between 1-7 \n")
    ship_three_column = input("Enter ship column between A-G \n").upper()
    while ship_three_column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Incorrect input")
        ship_three_column = input("Enter ship column between A-G \n").upper()
    ship_three_position = (int(ship_three_row)-1, letters_to_numbers[ship_three_column])
    print("Ship three in position")
    # Ship Four
    print("Time to position our fourth ship")
    ship_four_row = input("Enter ship row between 1-7 \n")
    while ship_four_row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Incorrect input")
        ship_four_row = input("Enter ship row between 1-7 \n")
    ship_four_column = input("Enter ship column between A-G \n").upper()
    while ship_four_column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Incorrect input")
        ship_four_column = input("Enter ship column between A-G \n").upper()
    ship_four_position = (int(ship_four_row)-1, letters_to_numbers[ship_four_column])
    print("Ship four in position")
    return [ship_one_position, ship_two_position, ship_three_position, ship_four_position]


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


# create_ships(COMPUTER_BOARD)
# turns = 18
# print("Ahoy admiral, prepare for war! It's time for us to hide our own ships. Pick 4 locations by picking a row and column, and make sure they aren't too easily found.")
# print_board(COMPUTER_BOARD)
# print("We have 18 shots for the heavy artillery and reconnaissance tells us there are 4 enemy ships lurking in the area. A blank map of the sea is below, and the gunners are standing by--so it's up to you to find the enemy!")


# while turns > 0:
#     print_board(GUESS_BOARD)
#     row, column = get_ship_location()
#     if GUESS_BOARD[row][column] == "-":
#         print("Uh...you already guessed that. Are you ok admiral?")
#     elif COMPUTER_BOARD[row][column] == "X":
#         print("A hit! Well shot, sir, ship sunk.")
#         GUESS_BOARD[row][column] = "X"
#         turns -= 1
#     else:
#         print("No luck sir, shot missed.")
#         GUESS_BOARD[row][column] = "-"
#         turns -= 1
#     if count_hit_ships(GUESS_BOARD) == 4:
#         print("That's the last of them sir, we've done it! All battleships sunk, we've won!")
#         break

#     print(f"You have {turns} turns left. Your updated sea map is below.")
#     if turns == 0:
#         print("We're out of time. We ran out of turns, so the enemy has escaped with their remaining vessels.")

print(hide_ships())

