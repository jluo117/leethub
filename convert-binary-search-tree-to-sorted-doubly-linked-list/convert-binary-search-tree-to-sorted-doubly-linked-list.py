"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.head = None
        self.tail = None
        def helper(root):
            if root == None:
                return
            helper(root.left)
            if self.tail:
                self.tail.right = root
                root.left = self.tail
            else:
                self.head = root
            self.tail = root
            helper(root.right)
            
                
        helper(root)
        if root == None:
            return None
        self.tail.right = self.head
        self.head.left = self.tail
        return self.head
                
        