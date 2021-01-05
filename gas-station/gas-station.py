class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        postCost = []
        for g ,c in zip(gas,cost):
            postCost.append(g-c)
        if sum(postCost) < 0:
            return -1
        back = 0
        maxBack = 0
        maxIndex = -1
        for index in range(len(postCost)-1,-1,-1):
            back += postCost[index]
            if back >= maxBack:
                
                maxBack = back
                maxIndex = index
           
        return maxIndex
        
