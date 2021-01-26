class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        maxGain = 0
        curGain = 0
        L = 0
        R = 0
        while R < len(customers):
            if (R - L) + 1 > X:
                if grumpy[L] == 1:
                    curGain -= customers[L]
                L += 1
            if grumpy[R] == 1:
                curGain += customers[R]
            maxGain = max(curGain,maxGain)
            R += 1
        for c,g in zip(customers,grumpy):
            if g == 0:
                maxGain += c
        return maxGain
                
        
        
