## Linked List

### Date: 07/27/2023

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm, zero = dict(), Node(0)

        curr, copy = head, zero
        while curr:
            copy.next = Node(curr.val)
            hm[curr] = copy.next
            curr, copy = curr.next, copy.next

        curr, copy = head, zero.next
        while curr:
            copy.random = hm[curr.random] if curr.random else None
            curr, copy = curr.next, copy.next
        
        return zero.next