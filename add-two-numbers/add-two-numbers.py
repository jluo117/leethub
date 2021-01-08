# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
2-4-3
5-6-6
​
7-0-0-1
​
​
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(l1,l2,carry):
            if not l1 and not l2 and carry != 0:
                newVal = carry
                newNode = ListNode(newVal)
                return newNode
            if not l1 and not l2 and carry == 0:
                return None
            if l1 and not l2:
                if carry != 0:
                    newVal = l1.val + carry
                    if newVal > 9:
                        carry = newVal // 10
                        newNode = ListNode(newVal%10)
                        newNode.next = helper(l1.next,l2,carry)
                        return newNode
                    else:
                        newNode = ListNode(newVal)
                        newNode.next = helper(l1.next,l2,0)
                        return newNode
                else:
                    newNode = ListNode(l1.val)
                    newNode.next = helper(l1.next,l2,0)
                    return newNode
            if l2 and not l1:
                if carry != 0:
                    newVal = l2.val + carry
                    if newVal > 9:
                        carry = newVal // 10
                        newNode = ListNode(newVal%10)
                        newNode.next = helper(l1,l2.next,carry)
                        return newNode
