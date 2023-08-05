## String
## 2 Pointers

### Date: 07/25/2023
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        # connect the tail to head
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        curr.next = head

        # move to the new head
        k = length - (k%length)
        while k > 0:
            curr = curr.next
            k -= 1

        # disconnect and return the new head
        newhead = curr.next
        curr.next = None
        return newhead
