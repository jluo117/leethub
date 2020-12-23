class Solution:
    def trap(self, height: List[int]) -> int:
        runningMax = 0
        ary=[]
        for h in height:
            ary.append(runningMax)
            runningMax = max(h,runningMax)
        
        runningMax = 0
        for i in range(len(height)-1,-1,-1):
            ary[i] = min(ary[i],runningMax)
            runningMax = max(height[i],runningMax)
        tolWater = 0
        for index in range(len(ary)):
            if ary[index] > height[index]:
                tolWater += ary[index]-height[index]
        return tolWater
