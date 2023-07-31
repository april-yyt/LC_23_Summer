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
    def connect(self, root: 'Node') -> 'Node':
        stack = [(root, 0)]
        ans = defaultdict(list)
        while stack:
            s, level = stack.pop()
            if not s:
                return root
            ans[level].append(s)
            if s.right:
                stack.append((s.right, level+1))
            if s.left:
                stack.append((s.left,level+1))
        for v in ans.values():
            for i in range(len(v)-1):
                v[i].next = v[i+1]
        return root
