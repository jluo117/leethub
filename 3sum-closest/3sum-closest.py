'''
1
-1,2,1,-4

-1,2,0 = 1
-1 + 2 + 0= 1

-4,-1,1,2

-1


-1 2

1,2
1

'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        dif = float('inf')
        nums.sort()
        for index in range(len(nums)):
            lowerVal = nums[index]
            L = 0
            R = len(nums)-1
            while L < R:
                if L == index:
                    L+= 1
                    continue
                if R == index:
                    R -= 1
                    continue
                checkNum = lowerVal + nums[L] + nums[R]
                if dif > abs(target-checkNum):
                    dif = abs(target-checkNum)
                    closest = checkNum
                if checkNum == target:
                    return target
                if checkNum > target:
                    R -= 1
                else:
                    L += 1
        return closest
            
        
        