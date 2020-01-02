#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (40.00%)
# Likes:    1271
# Dislikes: 80
# Total Accepted:    157.4K
# Total Submissions: 392.2K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
#
#
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
#
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
#
#
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [[0] * 10 for _ in range(9)]
        cols = [[0] * 10 for _ in range(9)]
        boxes = [[0] * 10 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                bx = r // 3
                by = c // 3

                if n != ".":
                    n = int(n)
                    rows[r][n] = 1
                    cols[c][n] = 1
                    boxes[3 * bx + by][n] = 1

        def dfs(x, y):
            if x == 9:
                return True

            ny = (y + 1) % 9
            nx = x + 1 if ny == 0 else x

            if board[x][y] != ".":
                return dfs(nx, ny)

            for i in range(1, 10):
                bx = x // 3
                by = y // 3
                boxkey = bx * 3 + by
                if not rows[x][i] and not cols[y][i] and not boxes[boxkey][i]:
                    rows[x][i] = 1
                    cols[y][i] = 1
                    boxes[boxkey][i] = 1
                    board[x][y] = str(i)
                    if dfs(nx, ny):
                        return True
                    rows[x][i] = 0
                    cols[y][i] = 0
                    boxes[boxkey][i]= 0
                    board[x][y] = "."
            return False

        dfs(0, 0)

# @lc code=end

