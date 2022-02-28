import random
from ascii import logo

grid = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

gameRun = True
winner = None
current_player = 'X'
gameOn = True
player_names = {}
name = None
name_two = 'Computer'

print(logo)
print('Welcome to Tic-Tac-Toe Game!\n')

def show_Board(grid):
    print("\n")
    print("\t     |     |")
    print(f"\t  {grid[0]}  |  {grid[1]}  |  {grid[2]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {grid[3]}  |  {grid[4]}  |  {grid[5]}")
    print('\t_____|_____|_____')
    print("\t     |     |")
    print(f"\t  {grid[6]}  |  {grid[7]}  |  {grid[8]}")
    print("\t     |     |")
    print("\n")




# TODO 1 Take user input
def take_Input(grid):
    global current_player
    if gameRun:
        if current_player == "X":
            input_name = name
        elif current_player == "O":
            input_name = name_two
        try:
            current_input = int(input(f'{input_name}, Input the number 1-9 representing the square: '))
            if grid[current_input - 1] == '-':
                grid[current_input - 1] = current_player
            else:
                print('Oops, This square is already marked.')

        except UnboundLocalError:
            pass


# TODO 2 Check for win or tie

def checkHorizontles(grid):
    global winner
    if grid[0] == grid[1] == grid[2] and grid[0] != "-":
        winner = grid[0]
        return True
    if grid[3] == grid[4] == grid[5] and grid[3] != "-":
        winner = grid[3]
        return True
    if grid[6] == grid[7] == grid[8] and grid[6] != "-":
        winner = grid[6]
        return True


def checkVerticals(grid):
    global winner
    if grid[0] == grid[3] == grid[6] and grid[0] != "-":
        winner = grid[0]
        return True
    if grid[1] == grid[4] == grid[7] and grid[1] != "-":
        winner = grid[1]
        return True
    if grid[2] == grid[5] == grid[8] and grid[2] != "-":
        winner = grid[2]
        return True


def checkDiagonal(grid):
    global winner
    if grid[0] == grid[4] == grid[8] and grid[0] != "-":
        winner = grid[0]
        return True
    if grid[2] == grid[4] == grid[6] and grid[2] != "-":
        winner = grid[2]
        return True


def checkForWin(grid):
    global gameRun
    if checkHorizontles(grid):
        show_Board(grid)
        if winner == 'X':
            print(f"The winner is {name}!")
        elif winner == 'O':
            print(f"The winner is {name_two}!")
        gameRun = False

    elif checkVerticals(grid):
        show_Board(grid)
        if winner == 'X':
            print(f"The winner is {name}!")
        elif winner == 'O':
            print(f"The winner is {name_two}!")
        gameRun = False

    elif checkDiagonal(grid):
        show_Board(grid)
        if winner == 'X':
            print(f"The winner is {name}!")
        elif winner == 'O':
            print(f"The winner is {name_two}!")

        gameRun = False


def checkIfTie(grid):
    global gameRunning
    if "-" not in grid:
        show_Board(grid)
        print("It is a tie!")
        gameRunning = False


# switch player
def switchPlayer():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

while gameOn:
    try:
        mode = int(input('Type 1 to play with bot, type 2 to play with friend: \n'))
    except ValueError:
        print('Please enter only 1 or 2\n')
        continue

    if mode == 1:
        gameRun = True
        grid = ['-', '-', '-',
                '-', '-', '-',
                '-', '-', '-']

        name = input('Input your name: ')
        player_names[f'{name}'] = 0
        player_names['Computer'] = 0
        while gameRun:
            show_Board(grid)
            take_Input(grid)
            checkForWin(grid)
            checkIfTie(grid)
            switchPlayer()
            computer(grid)
            checkForWin(grid)
            checkIfTie(grid)
    elif mode == 2:
        gameRun = True
        grid = ['-', '-', '-',
                '-', '-', '-',
                '-', '-', '-']

        name = input('Input Player 1 name: ')
        name_two = input('Input Player 2 name: ')
        player_names[f'{name}'] = 0
        player_names[f'{name_two}'] = 0
        while gameRun:
            show_Board(grid)
            take_Input(grid)
            checkForWin(grid)
            checkIfTie(grid)
            show_Board(grid)
            switchPlayer()
            take_Input(grid)
            checkForWin(grid)
            checkIfTie(grid)
            switchPlayer()
