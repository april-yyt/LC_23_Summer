## Linked List

### Date: 07/26/2023



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 2 ptrs

        # save the linked list in an array
        arr = []
        curr, length = head, 0
        while curr:
            arr.append(curr)
            curr, length = curr.next, length +1

        # using 2 ptrs to reorder
        left, right = 0, length -1
        last = head
        while left < right:
            arr[left].next = arr[right]
            left += 1
            if left == right:
                last = arr[right]
                break
            arr[right].next = arr[left]
            right -= 1
            last = arr[left]

        if last:
            last.next = None
