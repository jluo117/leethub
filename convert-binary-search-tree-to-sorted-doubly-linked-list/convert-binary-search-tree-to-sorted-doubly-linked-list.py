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
        if root == None:
            return None
        self.tail = None
        self.head = None
        def helper(node):
            if node.left == None:
                if self.tail == None:
                    self.tail = node
                    self.head = self.tail
                else:
                    self.tail.right = node
                    node.left = self.tail
                    self.tail = node
            else:
                helper(node.left)
                self.tail.right = node
                node.left = self.tail
                self.tail = node
            if node.right:
                helper(node.right)
            return
        helper(root)
        self.tail.right = self.head
        self.head.left = self.tail
        return self.head
                
        