'''
[1,2,1,3,5,6,4]

5 < 6
6
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[mid +1]:
                high = mid
            else:
                low = mid + 1
            
        return low