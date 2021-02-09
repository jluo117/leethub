# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        bounds ={root}
        def getLside(root):
            if root == None:
                return
            bounds.add(root)
            if root.left:
                getLside(root.left)
            elif root.right:
                getLside(root.right)
            else:
                return
        def getRside(root):
            if root == None:
                return
            bounds.add(root)
            if root.right:
                getRside(root.right)
            elif root.left:
                getRside(root.left)
            else:
                return
        getLside(root.left)
        getRside(root.right)
        order = [root.val]
        def preTravel(root):
            if root == None:
                return
            if root in bounds or (root.left == None and root.right == None):
                order.append(root.val)
                
            preTravel(root.left)
            preTravel(root.right)
        def postTravel(root):
            if root == None:
                return
            postTravel(root.left)
            postTravel(root.right)
            if root in bounds or (root.left== None and root.right == None):
                order.append(root.val)
        preTravel(root.left)
        postTravel(root.right)
        return order