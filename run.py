# Initial Comment

print("Hello")
from random import randint

PLAYER_BOARD = [[" "]*7 for x in range(7)]
GUESS_BOARD = [[" "]*7 for x in range(7)]


letters_to_numbers = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6}


def print_board(board):
    print("A B C D E F G")
    print("-------------")
    row_number = 1
    for row in board:
        print("|%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships():
    for ship in range(4):
        ship_row, ship_column = randint(0, 6), randint(0, 6)
        

def get_ship_location():
    pass

def count_hit_ships():
    pass

create_ships()
turns=10
# while turns>0:


print("Hello")