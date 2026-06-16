#!/usr/bin/python3
"""Solve the N queens puzzle using backtracking."""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed at board[row][col]."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n):
    """Find all solutions to the N queens puzzle and print them."""
    board = [-1] * n

    def backtrack(row):
        if row == n:
            solution = [[r, board[r]] for r in range(n)]
            print(solution)
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve(n)
