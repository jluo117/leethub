class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lastNum = None
        for num in nums:
            if lastNum == None:
                lastNum = num
                continue
            if num - lastNum > k:
                return lastNum + k
            else:
                k -= num-lastNum
                k += 1
                lastNum = num
        return lastNum + k
        
        