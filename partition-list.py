# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
