# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        treeSums = {}
        def helper(root):
            if root == None:
                return 0
            Lsum = helper(root.left)
            Rsum = helper(root.right)
            subSum = Lsum + Rsum + root.val
            if subSum in treeSums:
                treeSums[subSum] += 1
            else:
                treeSums[subSum] = 1
            return subSum
        helper(root)
        maxFreq = 0
        for val in treeSums:
            maxFreq = max(treeSums[val],maxFreq)
        res = []
        for val in treeSums:
            if treeSums[val] == maxFreq:
                res.append(val)
        return res
