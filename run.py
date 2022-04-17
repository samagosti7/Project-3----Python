"""Initial Comment
X for placed battleship and hit battleship
' ' for available
"-" for miss """

from random import randint

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
    ship_positions = []
    print("Time to position our first ship.")
    ship_one_row = input("Enter ship row between 1-7 \n")
    while ship_one_row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid input, try again")
        ship_one_row = input("Enter ship row between 1-7 \n")
    ship_one_column = input("Enter ship column between A-G \n").upper()
    while ship_one_column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Invalid input, try again")
        ship_one_column = input("Enter ship column between A-G \n").upper()
    ship_one_position = (
        int(ship_one_row)-1, letters_to_numbers[ship_one_column]
    )
    print("Ship one in position")
    ship_positions.append(ship_one_position)
    # Ship Two
    print("Time to position our second ship")
    ship_two_row = input("Enter ship row between 1-7 \n")
    while ship_two_row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid input, try again")
        ship_two_row = input("Enter ship row between 1-7 \n")
    ship_two_column = input("Enter ship column between A-G \n").upper()
    while ship_two_column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Invalid input, try again.")
        ship_two_column = input("Enter ship column between A-G \n").upper()
    ship_two_position = (
        int(ship_two_row)-1, letters_to_numbers[ship_two_column]
    )
    print("Ship two in position")
    ship_positions.append(ship_two_position)
    # Ship Three
    print("Time to position our third ship")
    ship_three_row = input("Enter ship row between 1-7 \n")
    while ship_three_row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid input, try again")
        ship_three_row = input("Enter ship row between 1-7 \n")
    ship_three_column = input("Enter ship column between A-G \n").upper()
    while ship_three_column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Invalid input, try again")
        ship_three_column = input("Enter ship column between A-G \n").upper()
    ship_three_position = (
        int(ship_three_row)-1, letters_to_numbers[ship_three_column]
    )
    print("Ship three in position")
    ship_positions.append(ship_three_position)
    # Ship Four
    print("Time to position our fourth ship")
    ship_four_row = input("Enter ship row between 1-7 \n")
    while ship_four_row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid input, try again")
        ship_four_row = input("Enter ship row between 1-7 \n")
    ship_four_column = input("Enter ship column between A-G \n").upper()
    while ship_four_column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Invalid input, try again")
        ship_four_column = input("Enter ship column between A-G \n").upper()
    ship_four_position = (
        int(ship_four_row)-1, letters_to_numbers[ship_four_column]
    )
    print("Ship four in position")
    ship_positions.append(ship_four_position)
    while (
        ship_positions[0] == ship_positions[1] or
        ship_positions[0] == ship_positions[2] or
        ship_positions[0] == ship_positions[3]
    ):
        ship_positions[0] = randint(0, 6), randint(0, 6)
    while (
        ship_positions[1] == ship_positions[0] or
        ship_positions[1] == ship_positions[2] or
        ship_positions[1] == ship_positions[3]
    ):
        ship_positions[1] = randint(0, 6), randint(0, 6)
    while (
        ship_positions[2] == ship_positions[0] or
        ship_positions[2] == ship_positions[1] or
        ship_positions[2] == ship_positions[3]
    ):
        ship_positions[2] = randint(0, 6), randint(0, 6)
    while (
        ship_positions[3] == ship_positions[0] or
        ship_positions[3] == ship_positions[1] or
        ship_positions[3] == ship_positions[3]
    ):
        ship_positions[3] = randint(0, 6), randint(0, 6)
    return ship_positions


def create_ships(board):
    for x in range(4):
        ship_row, ship_column = randint(0, 6), randint(0, 6)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 6), randint(0, 6)
        board[ship_row][ship_column] = "X"


def get_ship_location():
    row = input("Enter ship row guess between 1 and 7:  \n")
    while row not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid input")
        row = input("Enter ship row guess between 1 and 7:  \n")
    column = input("Enter ship column guess between A-G:  \n").upper()
    while column not in ["A", "B", "C", "D", "E", "F", "G"]:
        print("Invalid input")
        column = input("Enter ship column guess between A-G:  \n").upper()
    return int(row)-1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


create_ships(COMPUTER_BOARD)
TURNS = 24
COMPUTER_COUNT = 0
print(
    "Ahoy admiral, prepare for war! It's time for us to hide our ships."
    " Pick 4 locations by picking a row and column. Note that placing two"
    " ships on the same tile is impossible--if you assign two vessels the same"
    " location, one will then defer to a random location in the ocean."
    )
computer_guess_list = hide_ships()
print(computer_guess_list)
print(
    "We have 24 shots for the heavy artillery and reconnaissance tells us"
    " there are 4 enemy ships lurking in the area. A blank map of the sea is"
    " below, and the gunners are standing by--it's up to you to find the enemy"
    ". Good luck.")
print_board(COMPUTER_BOARD)

while TURNS > 0:
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == "-":
        print("Uh...you already guessed that. Are you ok admiral?")
    elif COMPUTER_BOARD[row][column] == "X":
        print("A hit! Well shot, sir, ship sunk.")
        GUESS_BOARD[row][column] = "X"
        computer_guess = randint(0, 6), randint(0, 6)
        if computer_guess in computer_guess_list:
            COMPUTER_COUNT += 1
            print(
                "Some bad news--the enemy sunk one of ours. They've hit"
                "f{COMPUTER_COUNT} of our ships total so far.")
        else:
            print("Some good news--the enemy has missed!")
        TURNS -= 1
    else:
        print("No luck sir, shot missed.")
        GUESS_BOARD[row][column] = "-"
        computer_guess = randint(0, 6), randint(0, 6)
        if computer_guess in computer_guess_list:
            COMPUTER_COUNT += 1
            print(
                "Some bad news--the enemy sunk one of ours. They've hit"
                "f{COMPUTER_COUNT} of our ships total so far.")
        else:
            print("Some good news--the enemy has missed!")
        TURNS -= 1

    if count_hit_ships(GUESS_BOARD) == 4:
        print(
            "Alas, that's the last of them sir, we've done it! All enemy"
            "battleships sunk, we've won!")
        break
    if COMPUTER_COUNT == 4:
        print(
            "We are finished--thats the last of our navy sinking to the"
            "depths. It's been an honor, sir, but the enemy has won.")
        break
    print(f"We have {TURNS} shots left. Your updated sea map is below.")
    if TURNS == 0:
        print(
            "That's it, we're out of time. We ran out of turns, so both we"
            "and the enemy will live to sail another day.")
        break
