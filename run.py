from random import randint

# Computer board for generated ship locations that is hidden from user
computer_board = [[" "] * 9 for x in range(9)]
# User Board that displays hits and misses
user_board = [[" "] * 9 for i in range(9)]
turns = 30

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


# Funtion that starts the game
def start_game():
    global turns
    print("----- Game Mode: Starting turns = " + str(turns))
    print_board(user_board)
    plot_ships(computer_board)
    while turns > 0:
        print('Guess a battleship location')
        row, column = plot_coordinates()
        if user_board[row][column] == "-":
            print(", You guessed that one already.")
        elif computer_board[row][column] == "X":
            print("**** Hit ****")
            user_board[row][column] = "X" 
            turns -= 1  
        else:
            print(", YOU MISSED!")
            user_board[row][column] = "-"   
            turns -= 1     
        if check_hits(user_board) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        print_board(user_board)
        if turns == 0:
            print("You ran out of turns")
            replay_game = input("Do you wish to play again? y/n: ")
            if replay_game.upper() == "Y":
            restart_game()

# Function that allows the user to restart game
def restart_game():
    print("restart game")
    global turns
    turns = 30
    print(turns) 
    global user_board
    global computer_board
    user_board = [[" "] * 9 for i in range(9)]
    computer_board = [[" "] * 10 for x in range(9)]
    print(user_board)
    print(computer_board)
    start_game()


# Function that generates menu for user interface to allow for better UX
def show_menu():
    global name
    clear_screen()
    print("--- BATTLESHIPS ---")
    print(" ")
    print("   Hello! " + name)
    choice = input("a. play game     b. configure difficulty     c. Set name \n")
    
    if choice.upper() == "A":
        start_game()
    elif choice.upper() == "B":
        configure_difficulty()
    elif choice.upper() == "C":
        name = input("Enter Name: ")
        show_menu()
