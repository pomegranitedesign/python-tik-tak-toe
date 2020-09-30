# --- Global Variables --- 
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
game_running = True
winner = None

# Who's turn is it (by default its O's turn look below).
current_player = 'O'


def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def handle_turn(current_player):
    print(current_player + 's turn.')
    position = int(input('Choose a position from 1 to 9: ')) - 1

    if position not in [number for number in range(0, 9)]:
        position = int(input('Invalid input, please choose a position from 1 to 9: ')) - 1

    if board[position] != '-':
        print("The cell is already used")
    else:
        board[position] = current_player
    display_board()  # Update the board with a new player (O or X)


def check_game_over():
    check_win()
    check_tie()

# Flip player's turn from O to X and vice-versa.
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


def check_win():
    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()

    # check cols
    col_winner = check_cols()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    # Set up the global variables.
    global game_running

    # Check if any of the rows have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'

    # if any of the rows do have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_running = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_cols():
    # Set up the global variables
    global game_running

    # Check if any of the rows have all the same values (and is not empty)
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'

    # if any of the rows do have a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_running = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    # Set up the global variables
    global game_running

    # Check if any of the rows have all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'

    # if any of the rows do have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_running = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_tie():
    global game_running
    if '-' not in board:
        game_running = False
    return


def play_game():
    display_board()  # Display initial board

    # While the game is still running
    while game_running:
        handle_turn(current_player)  # Handle the player turn
        check_game_over()  # Check if the game has ended
        flip_player()  # Flip the current player

    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('This is a tie!')


# Start playing the game.
play_game()
