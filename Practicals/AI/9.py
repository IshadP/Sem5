def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1 

            if solve_n_queens_util(board, col + 1, N):
                return True

            board[i][col] = 0  

    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist")
        return False

    print_solution(board, N)
    return True

def print_solution(board, N):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

N = 12
solve_n_queens(N)
