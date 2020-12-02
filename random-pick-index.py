class Solution:
​
    def __init__(self, nums: List[int]):
        self.table = {}
        for index in range(len(nums)):
            if nums[index] in self.table:
                self.table[nums[index]].append(index)
            else:
                self.table[nums[index]] = [index]
        
​
    def pick(self, target: int) -> int:
        return random.choice(self.table[target])
        
​
​
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
