"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
​
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visit = set()
        while p != None:
            visit.add(p)
            p = p.parent
        while q != None:
            if q in visit:
                return q
            q = q.parent
        return None
        
