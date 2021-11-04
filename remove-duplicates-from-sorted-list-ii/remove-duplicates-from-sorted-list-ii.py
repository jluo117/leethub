# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        lastValid = None
        curVal = None
        curNode = head
        while curNode and curNode.next:
            if curNode.next.val == curNode.val:
                upperPoint = curNode
                while upperPoint and upperPoint.val == curNode.val:
                    upperPoint = upperPoint.next
                if lastValid == None:
                    head = upperPoint
                else:
                    lastValid.next = upperPoint
                curNode = upperPoint
            else:
                lastValid = curNode
                curNode = curNode.next
        return head
                
        