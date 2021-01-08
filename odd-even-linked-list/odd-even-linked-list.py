# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        def getTailandCount (head):
            if head.next == None:
                return head , 1
            tail , count = getTailandCount(head.next)
            return tail, count + 1
        tail , count = getTailandCount(head)
        prev = None
        nextVal = head
        curCount = 1
        while curCount <= count:
            
            if curCount % 2 == 1:
                prev = nextVal
                nextVal = nextVal.next
            else:
                if nextVal == tail:
                    break
                tmp = nextVal
                prev.next = nextVal.next
                nextVal.next = None
                tail.next = nextVal
                tail = nextVal
                nextVal = prev.next
            curCount += 1
        return head
        
