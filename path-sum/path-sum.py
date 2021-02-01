# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def helper(root,rem):
            if root == None and rem == 0:
                return True
            if root == None:
                return False
            if root.left == None:
                return helper(root.right,rem-root.val)
            if root.right == None:
                return helper(root.left,rem-root.val)
            return helper(root.left,rem-root.val) or helper(root.right,rem-root.val)
        return helper(root,targetSum)
        