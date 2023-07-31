## Linked List

### Date: 07/27/2023


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = head

        def flatLayer(node):
            prev = node
            while node:
                if node.child is not None:
                    end = flatLayer(node.child)
                    end.next = node.next
                    if node.next:
                        node.next.prev = end
                    node.next = node.child
                    node.child.prev = node
                    prev = end
                    node.child = None
                    node = end.next
                else:
                    prev = node
                    node = node.next
            return prev
        
        flatLayer(head)
        return head