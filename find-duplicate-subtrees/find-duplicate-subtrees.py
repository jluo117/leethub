# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        seenVal = set()
        addedSet = set()
        sol = []
        def helper(root):
            if root == None:
                
                return "None"
            Lnode = helper(root.left)
            Rnode = helper(root.right)
            res = Lnode+'L'+Rnode+'R'+str(root.val)
            if res in seenVal:
                if res not in addedSet:
                    addedSet.add(res)
                    sol.append(root)
                return res
            seenVal.add(res)
            return res
        helper(root)
        return sol
        
