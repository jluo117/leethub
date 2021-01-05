# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
​
​
'''
143252
​
122435
​
Atail 2
prev.next = curNode.next
curNode
tailNext = Atail.next
Atail.next = curNode
curNode.next = tailNext
'''
​
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        newNode = None
        newNodeHead = None
        prev = None
        curNode = head
        while curNode:
            if curNode.val >= x:
                if newNode == None:
                    newNode = ListNode(curNode.val)
                    newNodeHead = newNode
                else:
                    newNode.next = ListNode(curNode.val)
                    newNode = newNode.next
                if curNode == head:
                    head=head.next
                    curNode = head
                else:
                    prev.next = curNode.next
                    curNode = curNode.next
            else:
                prev = curNode
                curNode = curNode.next
        if newNodeHead != None:
            if prev == None:
                return newNodeHead
            prev.next = newNodeHead
        return head
        
