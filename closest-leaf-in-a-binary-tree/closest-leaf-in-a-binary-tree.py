# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = {}
        visit = set()
        leaf = set()
        def helper(root,parent):
            if root == None:
                return
            if parent != None:
                graph[root.val] = [parent.val]
            else:
                graph[root.val] = []
            if root.left == None and root.right == None:
                leaf.add(root.val)
            if root.left:
                graph[root.val].append(root.left.val)
            if root.right:
                graph[root.val].append(root.right.val)
            helper(root.left,root)
            helper(root.right,root)
        def findNode(root):
            if root == None:
                return None
            if root.val == k:
                return root
            
            res = findNode(root.left)
            if res != None:
                return res
            res = findNode(root.right)
            if res != None:
                return res
        helper(root,None)
        targetNode = findNode(root)
        if targetNode.val in leaf:
            return targetNode.val
        order = [targetNode.val]
        while order:
            newOrder = []
            for val in order:
                if val in leaf:
                    return val
                for lookUp in graph[val]:
                    if lookUp in visit:
                        continue
                    visit.add(lookUp)
                    newOrder.append(lookUp)
            order = newOrder
        return -1
        
        
        
        
        
        
       
                
