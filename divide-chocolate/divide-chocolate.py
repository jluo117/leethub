class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        tolSweet = sum(sweetness)
        minSweet = min(sweetness)
        def canSweet(curSweet):
            cuts = []
            runningSweet = 0
            for sweet in sweetness:
                if runningSweet + sweet >= curSweet:
                    if len(cuts) == K:
                        runningSweet += sweet
                    else:
                        endCut = runningSweet + sweet
                        cuts.append(endCut)
                        runningSweet = 0
                else:
                    runningSweet += sweet
            cuts.append(runningSweet)
            if len(cuts) != K + 1:
                return False
            return min(cuts) >= curSweet
        posSweet = minSweet
        while minSweet <= tolSweet:
            midPoint = (minSweet + tolSweet) // 2
            if canSweet(midPoint):
                posSweet = midPoint
                minSweet = midPoint + 1
            else:
                tolSweet = midPoint - 1
        return posSweet