# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 == None and t2 == None:
            return None
        if t1 == None:
            newNode = TreeNode(t2.val)
            newNode.left = self.mergeTrees(None,t2.left)
            newNode.right = self.mergeTrees(None,t2.right)
            return newNode
        if t2 == None:
            newNode = TreeNode(t1.val)
            newNode.left = self.mergeTrees(t1.left,None)
            newNode.right = self.mergeTrees(t1.right,None)
            return newNode
        newNode = TreeNode(t1.val+t2.val)
        newNode.left = self.mergeTrees(t1.left,t2.left)
        newNode.right = self.mergeTrees(t1.right,t2.right)
        return newNode
