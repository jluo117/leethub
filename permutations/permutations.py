class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seenVal = set()
        res = []
        def helper(curAry):
            if len(curAry) == len(nums):
                res.append(curAry)
                return
            for num in nums:
                if num not in seenVal:
                    seenVal.add(num)
                    helper(curAry+[num])
                    seenVal.remove(num)
        helper([])
        return res