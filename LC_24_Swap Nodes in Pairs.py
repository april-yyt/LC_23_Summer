## Linked List

### Date: 07/28/2023


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        curr = dummy

        while curr.next and curr.next.next:
            tmp = curr.next
            tmp1 = curr.next.next.next

            curr.next = curr.next.next
            curr.next.next = tmp
            tmp.next = tmp1
            curr = curr.next.next

        return dummy.next
