class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) -1 
        while R > L:
            P = L + int((R - L)/2)
            if nums[P] < nums[R]:
                R = P
            elif nums[P] > nums[R]:
                L = P + 1
            else:
                R -= 1
        return nums[L]
                
                
        
        