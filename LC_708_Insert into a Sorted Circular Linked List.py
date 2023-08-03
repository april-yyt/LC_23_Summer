## Linked List

### Date: 08/02/2023

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        v = Node(val, None)
        v.next = v
        if not head:
            return v 
        prev, cur = head, head.next
        while True:
            if prev.val <= val <= cur.val:
                break
            elif prev.val > cur.val and (val<=cur.val or val>=prev.val):
                break
            prev, cur = prev.next, cur.next
            if prev == head:
                break 
        prev.next = v
        v.next = cur 
        return head