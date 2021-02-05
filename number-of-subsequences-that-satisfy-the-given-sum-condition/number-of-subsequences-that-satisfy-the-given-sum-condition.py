class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        pos = 0
        L = 0
        R = len(nums)-1
        while L <= R:
            if nums[L] + nums[R] > target:
                R -= 1
            else:
                pos += (2**(R-L))
                L += 1
        return pos %((10 ** 9) + 7)
            
                
                    
        
        