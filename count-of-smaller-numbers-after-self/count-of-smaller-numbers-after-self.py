class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []
        sortedList = []
        for num in range (len(nums)-1,-1,-1):
            position=bisect.bisect_left(sortedList, nums[num])
            result.append(position)
            bisect.insort(sortedList,nums[num])
        return result[::-1]
        
