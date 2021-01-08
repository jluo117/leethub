class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')
        ndSmallest = float('inf')
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= ndSmallest:
                ndSmallest = num
            elif num > ndSmallest:
                return True
        return False
        
