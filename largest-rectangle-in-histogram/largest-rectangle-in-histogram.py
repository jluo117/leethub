class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        maxHeight = 0
        for index in range(len(heights)):
            start = index
            while stk and heights[index] < stk[-1][0]:
                val = stk.pop()
                maxHeight = max(maxHeight,((index-val[1]) * val[0]))
                start = val[1]
                if len(stk) == 0:
                    break
            stk.append((heights[index],start))
        while stk:
            val = stk.pop()
            maxHeight = max(maxHeight,((len(heights)-val[1]) * val[0]))
        return maxHeight
        
