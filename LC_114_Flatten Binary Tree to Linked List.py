## Linked List

### Date: 08/01/2023

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        # store the left and right subtree
        left = root.left
        right = root.right

        # treat the left subtree as the right
        root.left = None
        root.right = left

        # connect the original right subtree to the end of the right subtree
        p = root
        # itertae to the right most element
        while p.right:
            p = p.right
        # connect
        p.right = right
        
        

