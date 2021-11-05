class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        pro = 1
        L = 0
        if k == 0 or k== 1:
            return 0
        
        for right in range(len(nums)):
            pro *= nums[right]
            while pro >= k:
                pro /= nums[L]
                L += 1
            ans += right - L +1
        return ans
        