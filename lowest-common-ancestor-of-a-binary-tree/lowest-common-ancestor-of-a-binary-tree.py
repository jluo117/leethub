# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def helper(node):
            if node == None:
                return False
            Lres = helper(node.left)
            Rres = helper(node.right)
            if Lres and Rres:
                self.res = node
                return True
            if (Lres or Rres) and (node == p or node == q):
                self.res = node
                return True
            return Lres or Rres or node == p or node == q
        helper(root)
        return self.res
