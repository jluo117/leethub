# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        self.masterHead = head
        table = {}
        def helper(head,root):
            if (head,root) in table:
                return table[(head,root)]
            if head == None:
                return True
            if root == None:
                return False
            if head.val != root.val:
                newHead = self.masterHead
                if newHead.val == root.val:
                    res = helper(newHead.next,root.left) or helper(newHead.next,root.right)
                    table[(head,root)] = res
                    return res
                else:
                    res = helper(newHead,root.left) or helper(newHead,root.right)
                    table[(head,root)] = res
                    return res
            else:
                res = helper(head.next,root.left) or helper(head.next,root.right)
                if res == False:
                    newHead = self.masterHead
                    if newHead.val == root.val:
                        res = helper(newHead.next,root.left) or helper(newHead.next,root.right)
                        table[(head,root)] = res
                    else:
                        res = helper(newHead,root.left) or helper(newHead,root.right)
                        table[(head,root)] = res
                return res
        return helper(head,root)
