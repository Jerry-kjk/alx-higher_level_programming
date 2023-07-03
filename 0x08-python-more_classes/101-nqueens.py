#!/usr/bin/python3

"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    """
    Solve the N queens problem using backtracking
    """
    # Base case: If all queens are placed, print the solution
    if col >= N:
        solution = [[r, c] for c, r in enumerate(board)]
        print(solution)
        return True

    # Recursive case: Try placing a queen in each row of the current column
    for row in range(N):
        if is_safe(board, row, col):
            # Place the queen in board[row][col]
            board[row][col] = 1

            # Recur for the next column
            solve_nqueens(board, col + 1)

            # Backtrack and remove the queen from board[row][col]
            board[row][col] = 0

    return False


if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Read N from command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard NxN
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N queens problem
    solve_nqueens(board, 0)

