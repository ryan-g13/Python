from random import randint

'''This is a 1 player version of Battleship that currently only allows 4 turns to guess on a grid of 5 x 5
    Please enjoy responsibly'''

board = [] # empty gameboard list

for x in range(0, 5): # fill in board with "O"s
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row)) # remove commas and brackets from list of lists

print_board(board)

def random_row(board): # methods to generate the random row/column placement of battleship
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)    # generate the random row/column placement of battleship
ship_col = random_col(board)
#print(ship_row)  - removing location of ship in order to make game challenging!!!
#print(ship_col)

# Loop that defines the game "Editable" range for turns # and
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):  #logic test for out of bounds
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":    #logic test for if already guessed there
            print( "You guessed that one already." )
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 3:   #game over test based on turn count
            print("Game Over")
    print_board(board)

'''Future enhancements
enhancements—maybe you can think of some more!

    Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

    Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

    Make your game a two-player game.

    Use functions to allow your game to have more features like rematches, statistics and more!
'''