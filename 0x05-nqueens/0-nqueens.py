#!/usr/bin/env python3
"""backtracking algorithm to solve n queens problem"""
import sys


def print_usage_and_exit():
    """Prints usage and exits"""
    print("Usage: nqueens N")
    sys.exit(1)


def validate_input():
    """Validates command-line input and returns N if valid"""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def is_safe(board, row, col, N):
    """Checks if a queen can be placed on board[row][col]"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, N, solutions):
    """Recursively attempts to place queens and store solutions"""
    if col == N:
        # Found a solution; convert to desired format
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(board, col + 1, N, solutions)
            board[i][col] = 0  # Backtrack


def main():
    """Main function"""
    N = validate_input()

    # Initialize board with zeros
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
