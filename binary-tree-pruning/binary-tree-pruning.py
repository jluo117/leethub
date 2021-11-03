# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node):
            if node == None:
                return False
            L_res = helper(node.left)
            R_res = helper(node.right)
            if not L_res:
                node.left = None
            if not R_res:
                node.right = None
            if node.val == 1:
                return True
            return L_res or R_res
        if helper(root):
            return root
        return None
        