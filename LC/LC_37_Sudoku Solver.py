## Array

### Date: 07/18/2023

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # solution with recursion
        n = 9

    def isValid(row, col, ch):
                row, col = int(row), int(col)
                
                for i in range(9):
                    
                    if board[i][col] == ch:
                        return False
                    if board[row][i] == ch:
                        return False
                    
                    if board[3*(row//3) + i//3][3*(col//3) + i%3] == ch:
                        return False
                
                return True
                
    def solve(row, col):
        # iterate over and recursion

        # first check if the given pos(row,col) is within the sudoku board
        if row == n:
            return True
        if col == n:
            return solve(row+1, 0)
        
        # for an empty cell, try to fill it with a number from 1 to 9 and check if valid
        if board[row][col] == ".":
            for i in range(1, 10):
                if isValid(row, col, str(i)):
                    board[row][col] = str(i)
                    
                    if solve(row, col + 1):
                        return True
                    else:
                        board[row][col] = "."
            return False
        else:
            return solve(row, col + 1)

    solve(0, 0)