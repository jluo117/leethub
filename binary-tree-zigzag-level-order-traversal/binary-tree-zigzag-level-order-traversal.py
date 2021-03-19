# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        left = True
        res = []
        order = [root]
        while len(order):
            
            newRow = []
            if left:
                output = [node.val for node in order]
                res.append(output)
                left = False
            else:
                output = [order[index].val for index in range(len(order)-1,-1,-1)]
                res.append(output)
                left = True
            for node in order:
                if node.left:
                    newRow.append(node.left)
                if node.right:
                    newRow.append(node.right)
            order = newRow
        return res