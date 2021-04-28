class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxVal = 0
        for index in range(len(heights)):
            curHeight = heights[index]
            start = index
            while len(stk) and stk[-1][1] > curHeight:
                dis = index - stk[-1][0]
                maxVal = max(maxVal,dis*stk[-1][1])
                start = stk[-1][0]
                stk.pop()
            stk.append((start,curHeight))
        
        while len(stk):
            popVal = stk.pop()
            dis = len(heights)-popVal[0]
            maxVal = max(maxVal,dis*popVal[1])
        return maxVal
                
                
                
            