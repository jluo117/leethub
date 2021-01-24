'''
1->2->2->1
​
2->1 2->1
​
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        def findMidPoint(head):
            fast = head.next
            slow = head
            while fast:
                slow = slow.next
                if fast.next:
                    fast = fast.next.next
                else:
                    break
            return slow
        midPoint = findMidPoint(head)
        self.tail = None
        def reverseList(startNode):
            if startNode.next == None:
                self.tail = startNode
                return startNode
            outNode = reverseList(startNode.next)
            outNode.next = startNode
            startNode.next = None
            return startNode
        reverseList(midPoint)
        
        while self.tail and head != self.tail:
            if self.tail.val != head.val:
                return False
            self.tail = self.tail.next
            head = head.next
        return True
