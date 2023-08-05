## Sorting

### Date: 08/04/2023

class Solution:
    def generateTrees(self, n:int)-> List[TreeNode]:
        if n == 0: return[]
        return self.build(1,n) #create a [1,n] BST

    def build(self,lo:int,hi:int)->List[TreeNode]:
        res=[]
        #when lo>hi, there is no valid BST
        if lo > hi:
            res.append(None)
            return res
        
        #all possible roots
        for i in range(lo,hi+1):
            # recursively create all valid BST
            leftTree=self.build(lo,i-1)
            rightTree=self.build(i+1,hi)
            #list all possible combinations of left and right   
            for left in leftTree:
                for right in rightTree:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res

