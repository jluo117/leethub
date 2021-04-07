class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        taken = sum(cardPoints)
        res = 0
        windowVal = 0
        noTakeWindow = len(cardPoints) - k
        L = 0
        R = noTakeWindow
        for i in range(noTakeWindow):
            windowVal += cardPoints[i]
        res = max(res,taken-windowVal)
        while R < len(cardPoints):
            windowVal -= cardPoints[L]
            windowVal += cardPoints[R]
            L += 1
            R += 1
            res = max(res,taken-windowVal)
        return res
    
        