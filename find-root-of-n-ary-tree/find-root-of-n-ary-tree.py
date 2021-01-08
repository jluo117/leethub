"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
​
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        if tree == None:
            return None
        zeroFlag = False
        for node in tree:
            for child in node.children:
                if child.val == 0:
                    zeroFlag = True
                child.val *= -1
        correctNode = None
        for node in tree:
            if node.val >= 0:
                if node.val == 0 and zeroFlag != False:
                    continue
                correctNode = node
            else:
                node.val *= -1
        return correctNode
        
                    
                
    
            
