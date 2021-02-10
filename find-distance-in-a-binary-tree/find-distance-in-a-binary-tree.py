# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        self.parentNode = None
        def findChildren(root):
            if root == None:
                return False,False
            pVal = False
            qVal = False
            if root.val == p:
                pVal = True
            if root.val == q:
                qVal = True
            pStat,qStat = findChildren(root.left)
            pVal |= pStat
            qVal |= qStat
            pStat,qStat = findChildren(root.right)
            pVal |= pStat
            qVal |= qStat
            if pVal and qVal and self.parentNode == None:
                self.parentNode = root
            return pVal,qVal
        findChildren(root)
        def findp(root):
            if root == None:
                return -1
            if root.val == p:
                return 0
            Lval = findp(root.left)
            if Lval != -1:
                return Lval + 1
            Rval =findp(root.right)
            if Rval != -1:
                return Rval + 1
            return -1
        def findq(root):
            if root == None:
                return -1
            if root.val == q:
                return 0
            Lval = findq(root.left)
            if Lval != -1:
                return Lval + 1
            Rval = findq(root.right)
            if Rval != -1:
                return Rval + 1
            return -1
        return findp(self.parentNode) + findq(self.parentNode)
    
                
            
                