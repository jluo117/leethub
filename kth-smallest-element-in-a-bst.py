# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        def helper(root,rem):
            if root == None:
                return rem
            L = helper(root.left,rem)
            if L == -1:
                return -1
            if L == k:
                self.res = root.val
                return -1
            R = helper(root.right,L+1)
            return R
        helper(root,1)
        return self.res
