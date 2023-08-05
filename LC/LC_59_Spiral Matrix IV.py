## Array

### Date: 07/21/2023

""" Generate an m x n matrix that contains the integers 
in the linked list presented in spiral order (clockwise) """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        top, left = 0, 0
        down, right = len(matrix)-1, len(matrix[0])-1
        direction = 0
        curr = head
        while top <= down and left <= right:
            if direction == 0:
                for i in range(left, right+1): # from left to right
                    if curr:
                        matrix[top][i] = curr.val
                        curr = curr.next
                top += 1
            elif direction == 1:
                for i in range(top, down+1): # from top to bottom
                    if curr:
                        matrix[i][right] = curr.val
                        curr = curr.next
                right -= 1
            elif direction == 2: # from right to left
                for i in range(right, left-1, -1):
                    if curr:
                        matrix[down][i] = curr.val
                        curr = curr.next
                down -= 1
            elif direction == 3: # from bottom to top
                for i in range(down, top-1, -1):
                    if curr:
                        matrix[i][left] = curr.val
                        curr = curr.next
                left += 1
            direction = (direction + 1) % 4
        return matrix