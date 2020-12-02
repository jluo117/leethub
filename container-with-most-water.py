class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) -1
        maxVal = 0
        while L <= R:
            maxVal = max(maxVal,min(height[L],height[R])*(R-L))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return maxVal
        
