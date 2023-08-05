## Linked List
## 2 Pointers

### Date: 07/25/2023

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        List_A = headA
        List_B = headB

        while List_A != List_B:
            List_A = headB if List_A is None else List_A.next
            List_B = headA if List_B is None else List_B.next
        
        return List_A