"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        table = {}
        def helper(node):
            
            if node in table:
                return table[node]
            newNode = Node(node.val)
            table[node] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(helper(n))
            return newNode
        return helper(node)
        