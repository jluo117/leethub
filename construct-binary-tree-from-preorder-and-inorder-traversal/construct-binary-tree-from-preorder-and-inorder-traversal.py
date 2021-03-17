# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        table = {}
        for index in range(len(inorder)):
            table[inorder[index]] = index
        self.preOrderIndex = 0
        def helper(left,right):
            if left > right:
                return None
            curIndex = table[preorder[self.preOrderIndex]]
            newNode = TreeNode(preorder[self.preOrderIndex])
            self.preOrderIndex += 1
            newNode.left = helper(left,curIndex-1)
            newNode.right = helper(curIndex+1,right)
            return newNode
        return helper(0,len(preorder)-1)
            
            
            
            