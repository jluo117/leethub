# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        cur_node = head
        while cur_node != None:
            if cur_node.val == val:
                if prev == None:
                    head = head.next
                    cur_node = cur_node.next
                else:
                    prev.next = cur_node.next
                    cur_node = cur_node.next
            else:
                prev = cur_node
                cur_node = cur_node.next
        if prev == None:
            return None
        return head
        