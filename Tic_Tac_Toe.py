
import math

# Constants representing the players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def print_board(board):
    # Function to print the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("---------")

def evaluate(board):
    # Function to evaluate the current state of the board
    # Returns +10 if the computer wins, -10 if the player wins, and 0 for a tie or incomplete game
    for row in board:
        if row.count(PLAYER_X) == 3:
            return 10
        elif row.count(PLAYER_O) == 3:
            return -10

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == PLAYER_X:
            return 10
        elif board[0][col] == board[1][col] == board[2][col] == PLAYER_O:
            return -10

    if board[0][0] == board[1][1] == board[2][2] == PLAYER_X or board[0][2] == board[1][1] == board[2][0] == PLAYER_X:
        return 10
    elif board[0][0] == board[1][1] == board[2][2] == PLAYER_O or board[0][2] == board[1][1] == board[2][0] == PLAYER_O:
        return -10

    return 0

def is_moves_left(board):
    # Function to check if there are any remaining moves
    for row in board:
        if EMPTY in row:
            return True
    return False

def minmax_alpha_beta(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth  # Subtract depth to favor quicker wins
    if score == -10:
        return score + depth  # Add depth to favor delayed losses
    if not is_moves_left(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    best = max(best, minmax_alpha_beta(board, depth + 1, alpha, beta, False))
                    alpha = max(alpha, best)
                    board[i][j] = EMPTY

                    if beta <= alpha:
                        break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    best = min(best, minmax_alpha_beta(board, depth + 1, alpha, beta, True))
                    beta = min(beta, best)
                    board[i][j] = EMPTY

                    if beta <= alpha:
                        break
        return best

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_val = minmax_alpha_beta(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    return best_move

def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe with Alpha-Beta Pruning!")
    print_board(board)

    while is_moves_left(board):
        player_move = input("Enter your move coordinates (row col): ").split()
        row, col = int(player_move[0]), int(player_move[1])

        if board[row][col] != EMPTY:
            print("Invalid move. Try again.")
            continue

        board[row][col] = PLAYER_O
        print_board(board)

        if evaluate(board) == -10:
            print("You win!")
            return

        if not is_moves_left(board):
            print("It's a tie!")
            return

        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER_X
        print("Computer's move:")
        print_board(board)

        if evaluate(board) == 10:
            print("Computer wins!")
            return

        if not is_moves_left(board):
            print("It's a tie!")
            return

play_game()
