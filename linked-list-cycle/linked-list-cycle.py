# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
​
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        fast = head.next
        slow = head
        while fast:
            if fast == slow:
                return True
            slow = slow.next
            if fast.next == None:
                return False
            fast = fast.next.next
        return False
    
        
