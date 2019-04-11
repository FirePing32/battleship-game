from random import randint

#empty game board
board = []

#creating board
for x in range(0, 5):
    board.append(["O"] * 5)

# print a square board
def print_board(board):
    for row in board:
        print("".join(row))


print_board(board)

#position of ship, y-axis
def random_row(board):
    return randint(0, len(board) - 1)

#position of ship, x-axis
def random_col(board):
    return randint(0, len(board[0]) - 1)

#print position of ship
ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

#max 4 turns
for turn in range(4):

    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        #correct assumption
        print("Congratulations! You sank my battleship!")
        break
        #out of range
    elif guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        #already guessed
    elif board[guess_row][guess_col] == "X":
        print("You guessed that one already.")
        #unsuccessful attempts
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"

        if turn == 3:
            print("Game Over")
print_board(board)
