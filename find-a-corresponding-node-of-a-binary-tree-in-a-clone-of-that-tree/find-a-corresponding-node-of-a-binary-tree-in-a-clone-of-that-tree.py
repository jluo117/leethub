# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.correctNode = None
        def helper(origNode,cloneNode):
            if origNode == None:
                return
            if target == origNode:
                self.correctNode = cloneNode
            helper(origNode.left,cloneNode.left)
            helper(origNode.right,cloneNode.right)
            return
        helper(original,cloned)
        return self.correctNode
