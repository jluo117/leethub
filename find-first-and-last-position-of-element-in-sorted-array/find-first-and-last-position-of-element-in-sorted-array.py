class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findIndex(L,R):
            while L <= R:
                M = int((L+R)/2)
                if nums[M] == target:
                    return M
                if nums[M] < target:
                    L = M + 1
                else:
                    R = M - 1
            return -1
        start = findIndex(0,len(nums)-1)
        if start == -1:
            return [-1,-1]
        def lowerBound(start):
            smallest = start
            L = 0
            R = start
            while L < R:
                M = int((L+R)/2)
                if nums[M] < target:
                    L = M + 1
                elif nums[M - 1] < target:
                    return M
                else:
                    R = M -1
            return L
            
        def upperBound(start):
            biggest = start
            L = start
            R = len(nums)-1
            while L < R:
                M = int((L+R)/2)
                if nums[M] > target:
                    R = M - 1
                elif nums[M + 1] > target:
                    return M
                else:
                    L = M + 1
            
            return R
        return [lowerBound(start),upperBound(start)]