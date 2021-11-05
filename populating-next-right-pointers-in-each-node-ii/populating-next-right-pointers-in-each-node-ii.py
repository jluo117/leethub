"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root == None:
            return None
        order = [root]
        while len(order) > 0:
            prev = order[0]
            newOrder = []
            for index in range(1,len(order)):
                prev.next = order[index]
                prev = order[index]
            for node in order:
                if node.left:
                    newOrder.append(node.left)
                if node.right:
                    newOrder.append(node.right)
            order = newOrder
        return root
            
                
            
            
        