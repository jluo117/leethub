# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        table = {}
        for index in range(len(inorder)):
            table[inorder[index]] = index
        self.postOrderIndex = len(postorder)-1
        def helper(lowerLimit):
            curPostVal = postorder[self.postOrderIndex]
            if self.postOrderIndex == -1:
                return None
            if table[curPostVal] < lowerLimit:
                return None
            newNode = TreeNode(curPostVal)
            self.postOrderIndex -= 1
            newNode.right = helper(table[curPostVal])
            newNode.left = helper(lowerLimit)
            return newNode
        return helper(-1)
    