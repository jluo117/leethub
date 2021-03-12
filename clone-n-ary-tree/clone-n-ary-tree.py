"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        newNode = Node(root.val)
        if root.children:
            for child in root.children:
                newNode.children.append(self.cloneTree(child))
        return newNode