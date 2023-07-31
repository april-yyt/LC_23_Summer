## Linked List

### Date: 07/31/2023

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return 
        self.traverse(root.left, root.right)
        return root

    def traverse(self, node1, node2):
        if not node1 or not node2:
            return
        # connect the two node input
        node1.next = node2
        # connect the two subnodes with same parent node
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        # conect the two subnodes crossing the parent
        self.traverse(node1.right, node2.left)