# Tic_Tac_Toe.py

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or \
           board[0][i] == board[1][i] == board[2][i] != " ":
            return board[i][i]
    if board[0][0] == board[1][1] == board[2][2] != " " or \
       board[0][2] == board[1][1] == board[2][0] != " ":
        return board[1][1]
    return None

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn")
        row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
        
        if board[row][col] == " ":
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
    
    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
