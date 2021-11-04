# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.curSum = 0
        def helper(node):
            if node == None:
                return False
            if node.left == None and node.right == None:
                return True
            if helper(node.left):
                self.curSum += node.left.val
            helper(node.right)
            return False
        helper(root)
        return self.curSum