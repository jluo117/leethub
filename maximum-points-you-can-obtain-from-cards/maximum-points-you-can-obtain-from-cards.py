class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxVal = 0
        windowVal = 0
        cardSum = sum(cardPoints)
        windowSize = len(cardPoints) - k
        L = 0
        R = 0
        while R < len(cardPoints):
            if (R-L)+1 > windowSize:
                windowVal -= cardPoints[L]
                L += 1
            windowVal += cardPoints[R]
            if (R-L)+1 == windowSize:
                maxVal = max(maxVal,cardSum-windowVal)
            R += 1
        return maxVal
        