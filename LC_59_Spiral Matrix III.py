## Array

### Date: 07/21/2023


""" You will walk in a clockwise spiral shape to visit every position in this grid. 
Whenever you move outside the grid's boundary, 
we continue our walk outside the grid (but may return to the grid boundary later.). 
Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them
 """
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans =[]
        left, right = cStart, cStart+1
        top, bottom = rStart, rStart+1
        current = 1
        move = 0

        while current <= rows * cols:
            # fill top
            for i in range(left+move, right+1):
                if self.inbound(top, i, rows, cols):
                    ans.append([top, i])
                    current += 1
            left -= 1
            # fill right
            for i in range(top+1, bottom+1):
                if self.inbound(i, right, rows, cols):
                    ans.append([i, right])
                    current += 1
            top -= 1

            # fill bottom
            for i in range(right -1, left -1, -1):
                if self.inbound(bottom, i, rows, cols):
                    ans.append([bottom, i])
                    current += 1
            bottom += 1
            move = 1
        return ans

    def inbound(self, r, c, rows, cols):
        return 0 <= r < rows and 0 <= c < cols
