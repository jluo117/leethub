# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def checkSize(node):
            curNode = node
            count = 0
            while curNode and count < k:
                count += 1
                if count == k:
                    return curNode
                curNode = curNode.next
            return None
        def reverse(curHead):
            prev = None
            tl = None
            curNode = curHead
            while curNode:
                nextNode = curNode.next
                if prev == None:
                    prev = curNode
                    curNode.next = None
                    tl = curNode
                else:
                    curNode.next = prev
                    prev = curNode
                curNode = nextNode
            return prev,tl
                    
           
        curNode = head
        prev = None
        while curNode != None:
            getTail = checkSize(curNode)
            if getTail == None:
                return head
            nextVal = getTail.next
            getTail.next = None
            newHead,newTail = reverse(curNode)
            if prev == None:
                head = newHead
            else:
                prev.next = newHead
            prev = newTail
            newTail.next = nextVal
            curNode = nextVal
        return head
            
                
        