def is_valid(board, row, col, num):
    # Check if num is already present in the row
    for x in range(9):
        if board[row][x] == num:
            return False
    
    # Check if num is already present in the column
    for x in range(9):
        if board[x][col] == num:
            return False
    
    # Check if num is already present in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l[0], l[1] = row, col
                return True
    return False

def solve_sudoku(board):
    l = [0, 0]
    
    if not find_empty_location(board, l):
        return True
    
    row, col = l[0], l[1]
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False

def print_board(board):
    for row in board:
        print(row)

def get_custom_input():
    board = []
    print("Enter the Sudoku board (9x9), use 0 for empty cells:")
    for i in range(9):
        row = list(map(int, input().split()))
        board.append(row)
    return board

# Get custom input Sudoku board
board = get_custom_input()

# Solve the Sudoku puzzle
if solve_sudoku(board):
    print("Sudoku solved successfully:")
    print_board(board)
else:
    print("No solution exists for the given Sudoku board.")
