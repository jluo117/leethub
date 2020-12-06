"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
​
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        Lnode = self.connect(root.left)
        Rnode = self.connect(root.right)
        def mergeHelper(Lnode,Rnode):
            Lnode.next = Rnode
            if Lnode.right:
                if Rnode.left:
                    mergeHelper(Lnode.right,Rnode.left)
                    return
                if Rnode.right:
                    mergeHelper(Lnode.right,Rnode.right)
                    return
                return
            if Lnode.left:
                if Rnode.left:
                    mergeHelper(Lnode.left,Rnode.left)
                    return
                if Rnode.right:
                    mergeHelper(Lnode.left,Rnode.right)
                    return
                return
            return
        if Lnode != None and Rnode != None:
            mergeHelper(Lnode,Rnode)
        return root
                    
        
