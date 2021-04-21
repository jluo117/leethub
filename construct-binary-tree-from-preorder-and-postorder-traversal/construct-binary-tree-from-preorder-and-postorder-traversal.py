# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1
2 5
3 4
'''
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        postIndex = {}
        self.preIndex = 0
        for index in range(len(post)):
            postIndex[post[index]] = index
        def helper(curPost):
            curNode = TreeNode(pre[self.preIndex])
            self.preIndex += 1
            if self.preIndex >= len(pre):
                return curNode
            nextVal = pre[self.preIndex]
            postPos = postIndex[nextVal]
            if postPos > curPost:
                return curNode
            Lnode = helper(postPos)
            curNode.left = Lnode
            if self.preIndex >= len(pre):
                return curNode
            nextVal = pre[self.preIndex]
            postPos = postIndex[nextVal]
            if postPos > curPost:
                return curNode
            Rnode = helper(postPos)
            
            curNode.right = Rnode
            return curNode
        return helper(len(post)-1)
    
            
            
            
            
        