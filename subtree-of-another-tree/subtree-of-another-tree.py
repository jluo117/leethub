# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def helper(curNode,curSub):
            if curNode== None and curSub == None:
                return True
            if curNode == None or curSub == None:
                return False
            if curNode.val != curSub.val:
                return False
            return helper(curNode.left,curSub.left) and helper(curNode.right,curSub.right)
        def TreeTravel(curNode):
            if curNode == None:
                return False
            if helper(curNode,t):
                return True
            return TreeTravel(curNode.left) or TreeTravel(curNode.right)
        return TreeTravel(s)
        