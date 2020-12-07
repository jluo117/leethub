# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        curIndex = 1
        curNode = head
        prev = None
        while curIndex < m:
            prev = curNode
            curNode = curNode.next
            curIndex += 1
        def reverse(e,curNode,curIndex):
            prev = None
            tail = curNode
            while curIndex <= e:
                nextVal = curNode.next
                curNode.next = prev
                prev = curNode
                curNode = nextVal
                curIndex += 1
            tail.next = curNode
            return prev
        
        if prev == None:
            return reverse(n,curNode,curIndex)
        else:
            prev.next = reverse(n,curNode,curIndex)
            return head
            
                
            
        
        
