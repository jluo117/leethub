class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        good_pos = 0
        last_good = 0
        for index in range(len(nums)):
            if index == 0:
                good_pos += 1
                continue
            if nums[index] != nums[last_good]:
                nums[good_pos],nums[index] = nums[index],nums[good_pos]
                last_good = good_pos
                good_pos += 1
        print(nums)
        while len(nums) > good_pos:
            nums.pop()
        return good_pos
            
        