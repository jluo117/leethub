# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def get_k_list(node):
            head = node
            end = node
            for _ in range(k):
                if node == None:
                    return None,None
                end = node
                node = node.next
            return head,end
        def reverse_list(head):
            tl = head
            prev = None
            cur = head
            while cur != None:
                nextNode = cur.next
                cur.next = prev
                prev = cur
                cur = nextNode
            return prev,tl
        masterHead = head
        prev = None
        curNode = head
        while curNode != None:
            curHead,end  = get_k_list(curNode)
            if end == None:
                return masterHead
            nextNode = end.next
            end.next = None
            newhead,newTl = reverse_list(curHead)
            if prev:
                prev.next = newhead
            else:
                masterHead = newhead
            prev = newTl
            newTl.next = nextNode
            curNode = nextNode
        return masterHead
        
        
                
        