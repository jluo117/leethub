class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol = [[]]
        nums.sort()
        def helper(curAry,index):
            pickNum = set()
            for UpperIndex in range(index,len(nums)):
                if  nums[UpperIndex] not in pickNum:
                    newAry = curAry + [nums[UpperIndex]]
                    sol.append(newAry)
                    pickNum.add(nums[UpperIndex])
                    helper(newAry,UpperIndex+1)
        helper([],0)
        return sol
        