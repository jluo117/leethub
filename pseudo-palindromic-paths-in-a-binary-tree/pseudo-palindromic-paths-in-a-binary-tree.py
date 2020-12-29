# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        curTable = {}
        self.pos = 0
        def isPal():
            hasOdd = False
            for val in curTable:
                if curTable[val] % 2 != 0:
                    if hasOdd:
                        return False
                    hasOdd = True
            return True
        def helper(node):
            if node == None:
                return 
            if node.val not in curTable:
                curTable[node.val] = 1
            else:
                curTable[node.val] += 1
            if node.left == None and node.right == None:
                if isPal():
                    self.pos += 1
            else:
                helper(node.left)
                helper(node.right)
            curTable[node.val] -= 1
        helper(root)
        return self.pos
        
