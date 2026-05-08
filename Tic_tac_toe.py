board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
board_example = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
def get_valid_int(prompt):
    """Helper function to prevent crashes on non-integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
def check_move(board, move):
    if move < 0 or move > 8:
        return False
    return board[move] != "X" and board[move] != "O"
def reset_board():
    return [" ", " ", " ", " ", " ", " ", " ", " ", " "]


print("Welcome to Tic Tac Toe!")
while True:
    print("Player 1: X")
    print("Player 2: O")
    print("The board looks like this:")
    print_board(board)
    print("The example board looks like this:")
    print_board(board_example)
    for i in range(9):
        win_check = False
        if i % 2 == 0:
            player = "X"
        else:
            player = "O"

        move = get_valid_int(f"Player {player}, enter your move: "  )

        while not check_move(board, move):
            print("Invalid move! Try again.")
            move = get_valid_int(f"Player {player}, enter your move: "  )

        board[move] = player

        print_board(board)
        if (board[0] == board[1] == board[2] and board[0] != " " or 
            board[3] == board[4] == board[5] and board[3] != " " or
            board[6] == board[7] == board[8] and board[6] != " " or 
            board[0] == board[3] == board[6] and board[0] != " " or
            board[1] == board[4] == board[7] and board[1] != " " or
            board[2] == board[5] == board[8] and board[2] != " " or
            board[0] == board[4] == board[8] and board[0] != " " or
            board[2] == board[4] == board[6] and board[2] != " "):
            win_check = True
        if win_check:
            print(f"Player {player} wins!")
            break
        elif i == 8:
            print("It's a draw!")
            break   

    choice = input("Do you want to play again? (yes/no): ")
    if choice.lower() != "yes":
        break
    board = reset_board()
print("Thanks for playing!")
