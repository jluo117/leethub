# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        maxVal = float('inf')
        minVal = -float('inf')
        def helper(root,maxVal,minVal):
            if root == None:
                return True
            if root.val >= maxVal or root.val <= minVal:
                return False
            return helper(root.left,root.val,minVal) and helper(root.right,maxVal,root.val)
        return helper(root,maxVal,minVal)
        