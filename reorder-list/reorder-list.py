# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1,2,3,4 5
4 3

1 4 2 3


'''
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head == None:
            return
        stk = []
        curHead = head
        while curHead:
            stk.append(curHead)
            curHead = curHead.next
        needed = len(stk) // 2
        tailOrder = []
        for _ in range(needed):
            tailOrder.append(stk.pop())
        curHead = head
        for node in tailOrder:
            nextVal = curHead.next
            curHead.next = node
            node.next = nextVal
            curHead = nextVal
        curHead.next = None
            

        return
        
        """
        Do not return anything, modify head in-place instead.
        """
        