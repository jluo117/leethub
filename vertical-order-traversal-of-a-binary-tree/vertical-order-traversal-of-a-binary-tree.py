# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        table = {}
        self.minVal = float('inf')
        self.maxVal = -float('inf')
        def helper(vertical,depth,node):
            if node == None:
                return
            self.minVal = min(self.minVal,vertical)
            self.maxVal = max(self.maxVal,vertical)
            if vertical not in table:
                table[vertical] = [(depth,node.val)]
            else:
                table[vertical].append((depth,node.val))
            helper(vertical-1,depth+1,node.left)
            helper(vertical+1,depth+1,node.right)
        helper(0,0,root)
        res = []
        for i in range(self.minVal,self.maxVal+1):
            if i in table:
                row = [i[1] for i in sorted(table[i])]
                res.append(row)
        return res
            
        