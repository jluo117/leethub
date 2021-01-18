"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
​
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        def helper(node):
            while node.next:
                if node.child:
                    nextNode = node.next
                    node.child.prev = node
                    tail = helper(node.child)
                    node.next = node.child
                    tail.next = nextNode
                    nextNode.prev = tail
                    node.child = None
                    node = nextNode
                    
                else:
                    node = node.next
            if node.child:
                tail = helper(node.child)
                node.next = node.child
                node.child.prev = node
                node.child = None
                return tail
            return node
        helper(head)
        return head
        
        
