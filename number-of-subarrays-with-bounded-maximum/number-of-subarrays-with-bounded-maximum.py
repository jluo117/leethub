class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            curCount = 0
            tolCount = 0
            for num in nums:
                if num <= bound:
                    curCount += 1
                    tolCount += curCount
                else:
                    curCount = 0
            return tolCount
        return count(right) - count(left-1)
        