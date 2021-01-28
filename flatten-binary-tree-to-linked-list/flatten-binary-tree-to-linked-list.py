# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        order = []
        if root == None:
            return
        def helper(root):
            if root == None:
                return
            
            order.append(root)
            helper(root.left)
            helper(root.right)
        helper(root)
        prev = root
        root.left = None
        for index in range(1,len(order)):
            order[index].left = None
            prev.right = order[index]
            prev = prev.right
            prev.right = None
        
        
        """
        Do not return anything, modify root in-place instead.
        """
        