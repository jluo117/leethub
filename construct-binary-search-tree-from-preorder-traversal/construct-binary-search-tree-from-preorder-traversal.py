# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.cur_index = 0
        def helper(max_val,min_val):
            if self.cur_index == len(preorder):
                return None
            if preorder[self.cur_index] < min_val:
                return None
            if preorder[self.cur_index] > max_val:
                return None
            new_node = TreeNode(preorder[self.cur_index])
            self.cur_index += 1
            L = helper(preorder[self.cur_index-1],min_val)
            R = helper(max_val,preorder[self.cur_index-1])
            new_node.left = L
            new_node.right = R
            return new_node
                
        return helper(float('inf'),-float('inf'))
    