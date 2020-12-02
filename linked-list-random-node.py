# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:
​
    def __init__(self, head: ListNode):
        self.linkListSize = 0
        self.list = head
        while head:
            self.linkListSize += 1
            head = head.next
        
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        
​
    def getRandom(self) -> int:
        target = random.randint(0,self.linkListSize-1)
        curNode = self.list
        curCount = 0
        while curCount < target:
            curNode = curNode.next
            curCount += 1
        return curNode.val
        """
        Returns a random node's value.
        """
        
​
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
