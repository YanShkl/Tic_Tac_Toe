import random

grid = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

gameRun = True
winner = None
current_player = 'X'


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


show_Board(grid)


# TODO 1 Take user input
def take_Input(grid):
    current_input = int(input('Input the number 1-9 representing the square: '))
    if grid[current_input - 1] == '-':
        grid[current_input - 1] = current_player
    else:
        print('Oops, This square is already marked.')


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
        winner = grid[1]
        return True


def checkForWin(grid):
    global gameRun
    if checkHorizontles(grid):
        show_Board(grid)
        print(f"The winner is {winner}!")
        gameRun = False

    elif checkVerticals(grid):
        show_Board(grid)
        print(f"The winner is {winner}!")
        gameRun = False

    elif checkDiagonal(grid):
        show_Board(grid)
        print(f"The winner is {winner}!")
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


while gameRun:
    show_Board(grid)
    take_Input(grid)
    checkForWin(grid)
    checkIfTie(grid)
    switchPlayer()
    computer(grid)
    checkForWin(grid)
    checkIfTie(grid)
