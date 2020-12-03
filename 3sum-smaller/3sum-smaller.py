'''
[-2,0,1,3]
-2 
'''
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        pos = 0
        for pivot in range(len(nums)):
            L = pivot + 1
            R = len(nums) -1
            while L < R:
                if nums[L] + nums[R] + nums[pivot] >= target:
                    R -= 1
                else:
                    pos += R -L
                    L += 1
                    
        return pos
        
