## Linked List

### Date: 08/01/2023

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        digits = []

        # store the linkedlist elements in an array
        while head:
            digits.append(head)
            head = head.next

        # iterate from right most to left
        for i in range(len(digits)-1, -1, -1):
            # if 9, add to 10
            if digits[i].val == 9:
                digits[i].val = 0
                if i == 0:
                    return ListNode(1,digits[i])

            else:
                digits[i].val += 1
                return digits[0]