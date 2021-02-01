# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        def getDepth(root):
            if root == None:
                return 0
            return max(getDepth(root.left),getDepth(root.right))+1
        self.minStr = 'z' * getDepth(root)
        def helper(root,curStr):
            if root == None:
                self.minStr = min(self.minStr,curStr)
                return
            if root.left == None:
                helper(root.right,chr(root.val+97)+curStr)
                return
            if root.right == None:
                helper(root.left,chr(root.val+97)+curStr)
                return
            helper(root.left,chr(root.val+97)+curStr)
            helper(root.right,chr(root.val+97)+curStr)
        
        helper(root,"")
        return self.minStr
        