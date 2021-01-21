# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
​
    def __init__(self, root: TreeNode):
        self.stk = []
        while root:
            self.stk.append(root)
            root = root.left
        
        
​
    def next(self) -> int:
        grabVal = self.stk.pop()
        if grabVal.right:
            targetNode = grabVal.right
            while targetNode:
                self.stk.append(targetNode)
                targetNode = targetNode.left
        return grabVal.val
        
        """
        @return the next smallest number
        """
        
​
    def hasNext(self) -> bool:
        return len(self.stk) > 0
        """
        @return whether we have a next smallest number
        """
        
​
​
