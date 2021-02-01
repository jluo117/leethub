# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
[1]
[2,3]
[5,4]
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
#         if root == None:
#             return None
#         order = [root]
#         res = []
        
#         while len(order) > 0:
#             res.append(order[-1].val)
#             newOrder = []
#             for node in order:
#                 if node.left:
#                     newOrder.append(node.left)
#                 if node.right:
#                     newOrder.append(node.right)
#             order = newOrder
#         return res
        res = []
        def helper(root,depth):
            if root == None:
                return None
            if len(res) == depth:
                res.append(root.val)
            if root.right:
                helper(root.right,depth+1)
            if root.left:
                helper(root.left,depth+1)
            else:
                return
        helper(root,0)
        return res
        