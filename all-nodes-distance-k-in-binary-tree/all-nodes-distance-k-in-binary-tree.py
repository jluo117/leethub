# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parentNodes = {}
        def travel(root,prev):
            if root == None:
                return
            parentNodes[root] = prev
            travel(root.left,root)
            travel(root.right,root)
        visitNodes = set()
        res = []
        def findKneigh(k,node):
            if node in visitNodes:
                return
            if node == None:
                return
            if k == 0:
                res.append(node.val)
                return
            visitNodes.add(node)
            findKneigh(k-1,node.left)
            findKneigh(k-1,node.right)
            if node in parentNodes:
                findKneigh(k-1,parentNodes[node])
        travel(root,None)
        findKneigh(K,target)
        return res
            
            