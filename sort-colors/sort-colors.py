'''
202110
​
002112
​
001122
​
​
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        L = 0
        R = len(nums) -1
        while (nums[L] == 0):
            L += 1
            if L >= len(nums):
                return
        while nums[R] == 2:
            R -=1
            if R < 0:
                return
        pointer = L
        while pointer <= R:
            if nums[pointer] == 0:
                nums[pointer] , nums[L] = nums[L] , nums[pointer]
                L +=1
                if pointer < L:
                    pointer +=1
            elif nums[pointer] == 2:
                nums[pointer] , nums[R] = nums[R] , nums[pointer]
                R -= 1
            else:
                pointer += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        
