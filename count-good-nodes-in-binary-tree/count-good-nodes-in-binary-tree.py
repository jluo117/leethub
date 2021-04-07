# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        def helper(root,maxVal):
            if root == None:
                return
            if root.val >= maxVal:
                self.good += 1
                helper(root.left,root.val)
                helper(root.right,root.val)
            else:
                helper(root.left,maxVal)
                helper(root.right,maxVal)
        helper(root,-float('inf'))
        return self.good