class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for index in range(len(nums)-2):
            k = index+2
            for upper in range(index+1,len(nums)-1):
                if nums[index] == 0:
                    break
                while k < len(nums) and nums[index]+nums[upper] > nums[k]:
                    k += 1
                count += (k - upper - 1)
        return count
                
        