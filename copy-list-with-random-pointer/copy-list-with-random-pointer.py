"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
​
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        table = {}
        def helper(head):
            if head == None:
                return None
            if head in table:
                return table[head]
            newNode = Node(head.val)
            table[head] = newNode
            newNode.next = helper(head.next)
            newNode.random = helper(head.random)
            return newNode
        return helper(head)
    
        
