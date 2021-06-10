class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        needed = [0] * len(heights)
        for index in range(len(heights)-1,-1,-1):
            if index == len(heights)-1:
                continue
            needed[index] = max(needed[index+1],heights[index+1])
        res = []
        for index in range(len(heights)):
            if needed[index] < heights[index]:
                res.append(index)
        return res
        