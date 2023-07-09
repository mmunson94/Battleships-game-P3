from random import randint

# Computer board for generated ship locations that is hidden from user
computer_board = [[" "] * 9 for x in range(9)]
# User Board that displays hits and misses
user_board = [[" "] * 9 for i in range(9)]

# Function to print the board for user UX
def print_board(board):
    print(" ")
    print("B|A|T|T|L|E|S|H|I|P|S")
    print(" +-+-+-+-+-+-+-+-+-+")
    print("  A B C D E F G H J ")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1 
    print(" +-+-+-+-+-+-+-+-+-+")
    print(" ")

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'J': 8
}

# Function to take user input of coordinates for missile strikes
def plot_coordinates():
    row = input("Enter the row of the ship: ").upper()
    while row not in "123456789":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGHJ":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

# Function to generate ship locations on cpu board
def plot_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,8), randint(0,8)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = plot_coordinates()
        board[ship_row][ship_column] = "X"

# Function to determine whether a ship has been hit
def check_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count
