# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(L,R):
            if L == R:
                newNode = TreeNode(nums[L])
                return newNode
            midPoint = (L+R)//2
            if midPoint == L:
                newNode = TreeNode(nums[midPoint])
                newNode.right = helper(R,R)
                return newNode
            newNode = TreeNode(nums[midPoint])
            newNode.left = helper(L,midPoint-1)
            newNode.right = helper(midPoint+1,R)
            return newNode
        return helper(0,len(nums)-1)
        