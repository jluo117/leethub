# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lowest = None
        
        def helper(root):
            if root == None:
                return False
            
            Rcontain = helper(root.right)
            Lcontain = helper(root.left)
            if Rcontain and Lcontain:
                self.lowest = root
            if root == p:
                if Rcontain or Lcontain:
                    self.lowest = root
                return True
            if root == q:
                if Rcontain or Lcontain:
                    self.lowest = root
                return True
            return Rcontain or Lcontain
        helper(root)
        return self.lowest
