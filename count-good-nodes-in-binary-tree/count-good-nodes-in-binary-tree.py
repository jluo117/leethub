# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def helper(node,minVal):
            if node == None:
                return
            if node.val >= minVal:
                self.count += 1
            helper(node.right,max(node.val,minVal))
            helper(node.left,max(node.val,minVal))
        helper(root,-float('inf'))
        return self.count
        