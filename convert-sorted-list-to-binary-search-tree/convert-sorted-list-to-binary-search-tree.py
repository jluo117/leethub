# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        listAry = []
        while head:
            listAry.append(head.val)
            head = head.next
        
        def helper(L,R):
            if L == R:
                newNode = TreeNode(listAry[L])
                return newNode
            midPoint = (L+R)//2
            if midPoint == L:
                newNode = TreeNode(listAry[midPoint])
                newNode.right = helper(R,R)
                return newNode
            newNode = TreeNode(listAry[midPoint])
            newNode.left = helper(L,midPoint-1)
            newNode.right = helper(midPoint+1,R)
            return newNode
        if len(listAry) == 0:
            return None
        return helper(0,len(listAry)-1)