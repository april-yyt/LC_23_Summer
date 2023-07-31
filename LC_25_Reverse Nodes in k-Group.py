## Linked List

### Date: 07/26/2023



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a = b = ListNode()
        i = 0
        z = None

        # Reverse the k nodes
        while head:
            i = i + 1
            if i <= k:
                x = head.next
                head.next = z
                z = head
                head = x
            # assign the reversed nodes to the new linked list
            if i == k:
                b.next = z
                # take the ptr to the end of the reversed nodes:
                while b and b.next:
                    b = b.next
                z = None
                i = 0
        # finally reverse the nodes and assign the nodes
        zz = None
        while z:
            g = z.next
            z.next = zz
            zz = z
            z = g
        # assign the final nodes, length less than k
        b.next = zz
        
        return a.next
