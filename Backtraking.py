#sudoku solver

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(row, col, ch):
            for i in range(9):
                # Check row
                if board[row][i] == ch:
                    return False
                # Check column
                if board[i][col] == ch:
                    return False
                # Check 3x3 box
                r = 3 * (row // 3) + i // 3
                c = 3 * (col // 3) + i % 3
                if board[r][c] == ch:
                    return False
            return True

        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for ch in "123456789":
                            if is_valid(row, col, ch):
                                board[row][col] = ch
                                if backtrack():
                                    return True
                                board[row][col] = "."
                        return False
            return True

        backtrack()
