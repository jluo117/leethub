# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.runningSum = 0
        def helper(curStr,root):
            if root.left == None and root.right == None:
                curStr += str(root.val)
                self.runningSum += int(curStr)
                return
            if root.left:
                helper(curStr+str(root.val),root.left)
            if root.right:
                helper(curStr+str(root.val),root.right)
        if root == None:
            return 0
        helper("",root)
        return self.runningSum
