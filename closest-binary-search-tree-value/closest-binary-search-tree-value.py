# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.closest = float('inf')
        def helper(root):
            if root == None:
                return
            if abs(self.closest-target) > abs(root.val-target):
                self.closest = root.val
            if root.val < target:
                helper(root.right)
            else:
                helper(root.left)
        helper(root)
        return self.closest
