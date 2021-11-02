# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(node):
            if node == None:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)
        def create_balance(L,R):
            
            if L > R:
                return None
            if R == len(nodes):
                return None
            if L == R:
                newNode = TreeNode(nodes[L].val)
                return newNode
            mid_point = (L + R) //2
            newNode = TreeNode(nodes[mid_point].val)
            Lside = create_balance(L,mid_point-1)
            Rside = create_balance(mid_point+1,R)
            newNode.left = Lside
            newNode.right = Rside
            return newNode
        return create_balance(0,len(nodes)-1)
        
            
            
            