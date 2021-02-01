# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        res = []
        def getSum(stk):
            curVal = 0
            for val in stk:
                curVal += val
            return curVal
        def helper(root,stk):
            if root == None:
                if getSum(stk) == sum:
                    res.append(stk)
                    return
                else:
                    return
            if root.left == None:
                helper(root.right,stk+[root.val])
                return
            if root.right == None:
                helper(root.left,stk+[root.val])
                return
            helper(root.left,stk+[root.val])
            helper(root.right,stk+[root.val])
        helper(root,[])
        return res
        