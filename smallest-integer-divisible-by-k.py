class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0:
            return -1
        if K % 5 == 0:
            return -1
        past = set()
        curVal = 0
        while curVal not in past:
            past.add(curVal)
            curVal *= 10
            curVal += 1
            if curVal % K == 0:
                return len(str(curVal))
        return -1
        
