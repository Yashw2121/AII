def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens(board, row + 1, n):
                return True
            board[row] = -1

    return False

def print_solution(board, n):
    for row in range(n):
        row_str = ['Q' if col == board[row] else '.' for col in range(n)]
        print(" ".join(row_str))

def n_queens(n):
    board = [-1] * n
    if solve_n_queens(board, 0, n):
        print_solution(board, n)
    else:
        print("Solution does not exist.")

n = int(input("Enter the value of n: "))
n_queens(n)
