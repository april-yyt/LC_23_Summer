## Linked List

### Date: 07/30/2023

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(k-1):
            fast = fast.next
        
        tail = fast
        while tail.next:
            slow = slow.next
            tail = tail.next

        fast.val, slow.val = slow.val, fast.val
        return head