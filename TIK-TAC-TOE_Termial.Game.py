MAX_ROUNDS = 9
NUM_ROWS = 3
NUM_COLS = 3
NUM_POSITIONS = 9
ROW_POS = 0
COL_POS = 1


def display_board(board):
    """Displays the board's current state as a 3x3 grid"""

    print("     0 1 2 ")
    for row in range(0, NUM_ROWS):
        print("  {}  ".format(row), end="")
        for col in range(0, NUM_COLS):
            if col == 0:
                print(board[(row, col)], end="")
            else:
                print("|{}".format(board[(row, col)]), end="")
        print(" ")
        if row < NUM_ROWS - 1:
            print("    --+-+--")
    print()

def main():
    
    board = {
        (0,0): ' ', (0,1): ' ', (0,2): ' ',
        (1,0): ' ', (1,1): ' ', (1,2): ' ',
        (2,0): ' ', (2,1): ' ', (2,2): ' '
    }

    play_tic_tac_toe(board)

def reset_board(board):
    """Resets the board dict to its original state with each
    position being empty (i.e. the (row, column) key has a
    space character (' ') value)."""

    for keys in board:
        board[keys]=' '

def get_current_player(round):
    """Returns the mark of the player whose turn it is in the current
    round of the game."""

    if round % 2==0:
        return 'X'
    return 'O'

def get_position_choice(board, player_mark):
    """Prompts the user for a valid (row, col) board position. Prompts
    for row and column are repeated until valid position provided. The
    valid (row, col) position chosen is returned."""

    print(player_mark+',')
    key=(9,0)
    while (key not in board) or (board[key]!=' '):
        row= input("Choose your row: ")
        while row not in "012" or not(row.isnumeric()):
            row= input("Choose your row: ")
        col= input("Choose your column: ")
        while col not in "012" or not(col.isnumeric()):
            col= input("Choose your column: ")
        print("")
        row=int(row)
        col=int(col)
        key=(row,col)
    return key


def update_board(board, player_mark, position):
    """Updates the value at the key represented by position
    in board dictionary to player_mark."""

    board[position]=player_mark


def display_outcome(round):
    """Displays an outcome message for a completed Tic-tac-toe game. """

    if round%2==0:
        print("X wins!")
        print()
    elif round==MAX_ROUNDS:
        print("It's a draw!")
        print()
    else:
        print("O wins!")
        print()

def check_positions(pos1_value, pos2_value, pos3_value):

    """Returns True when all parameters have a value of 'X' or
    all parameters have a value of 'O'. Returns False for all
    other value combinations."""

    if pos1_value==pos2_value and pos2_value==pos3_value and pos1_value=="X":
        return True
    elif pos1_value==pos2_value and pos2_value==pos3_value and pos1_value=="O":
        return True
    else:
        return False

def is_game_complete(board):

    """Determines whether or not a winning configuration has been achieved in the game
    represented by the board. Returns True when a winning configuration is detected and
    False when no winning configuration exists on the board."""

    if check_positions(board[0,0],board[0,1],board[0,2])==True:
        return True
    elif check_positions(board[1,0],board[1,1],board[1,2])==True:
        return True
    elif check_positions(board[2,0],board[2,1],board[2,2])==True:
        return True
    elif check_positions(board[0,0],board[1,1],board[2,2])==True:
        return True
    elif check_positions(board[0,2],board[1,1],board[2,0])==True:
        return True
    elif check_positions(board[0,0],board[1,0],board[2,0])==True:
        return True
    elif check_positions(board[0,1],board[1,1],board[2,1])==True:
        return True
    elif check_positions(board[0,2],board[1,2],board[2,2])==True:
        return True
    else:
        return False


def play_tic_tac_toe(board):

    """Controls Tic-tac-toe games. This includes prompting player's for
    position choices, checking for winning game configurations, and outputting
    the outcome of a game."""
    
    print("Let's Play Tic-tac-toe!")
    print()
    finished=False

    while finished==False:
        game=False
        round=0

        while game==False and round<MAX_ROUNDS:
            player_mark=get_current_player(round)
            display_board(board)
            position=get_position_choice(board,player_mark)
            update_board(board, player_mark, position)
            game=is_game_complete(board)
            if game==False:
                round+=1
                
        display_board(board)
        display_outcome(round)
        finished=is_program_finished()
        if finished==False:
            reset_board(board)
    print("Goodbye.")

def is_program_finished():

    """Prompts the user with the message "Play again (Y/N)?". The question is repeated
    until the user enters a valid response (one of Y/y/N/n). The function
    returns False if the user enters 'Y' or 'y' and returns True if the user
    enters 'N' or 'n'."""

    play_again = input('Play again (Y/N)?')
    print()
    while play_again not in "YyNn":
        play_again = input('Play again (Y/N)?')
        print()
    if play_again in "Yy":
        return False
    else:
        return True

if __name__ == '__main__':

    main()
