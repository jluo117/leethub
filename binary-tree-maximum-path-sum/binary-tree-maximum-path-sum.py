# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.curMax = -float('inf')
        def helper(root):
            if root == None:
                return 0
            Lval = max(helper(root.left),0)
            Rval = max(helper(root.right),0)
            levelMax = root.val + Lval + Rval
            self.curMax = max(self.curMax,levelMax)
            return root.val + max(Lval,Rval)
            
        helper(root)
        return self.curMax
        
            
