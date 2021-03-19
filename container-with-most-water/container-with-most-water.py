class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height)-1
        maxWater = 0
        while L < R:
            maxWater = max(min(height[L],height[R])*((R-L)),maxWater)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return maxWater
        