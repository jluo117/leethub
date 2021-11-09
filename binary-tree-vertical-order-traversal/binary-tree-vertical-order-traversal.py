# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = {}
        if root == None:
            return None
        order = [(root,0)]
        while len(order):
            new_order = []
            for node in order:
                if node[1] not in table:
                    table[node[1]] = [node[0].val]
                else:
                    table[node[1]].append(node[0].val)
                if node[0].left:
                    new_order.append((node[0].left,node[1]-1))
                if node[0].right:
                    new_order.append((node[0].right,node[1]+1))
            order = new_order
        order = [val for val in table]
        order.sort()
        res = []
        for row in order:
            res.append(table[row])
        return res
        
            
            
        