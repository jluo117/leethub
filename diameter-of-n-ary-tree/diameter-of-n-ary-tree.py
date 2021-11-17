"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.max_val = 0
        def helper(node):
            if node == None:
                return 0
            heap = []
            for child in node.children:
                heapq.heappush(heap,helper(child))
                if len(heap) > 2:
                    heapq.heappop(heap)
            self.max_val = max(self.max_val, sum(heap))
            if len(heap):
                return max(heap) + 1
            return 1
        helper(root)
        return self.max_val
        """
        :type root: 'Node'
        :rtype: int
        """