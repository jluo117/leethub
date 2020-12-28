class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        table = {}
        def helper(index,prev):
            if (index,prev) in table:
                return table[(index,prev)]
            if index == len(costs):
                return 0
            cost = float('inf')
            for cIndex in range(len(costs[index])):
                if cIndex != prev:
                    cost = min(cost,helper(index+1,cIndex)+costs[index][cIndex])
            table[(index,prev)] = cost
            return cost
        return helper(0,-1)
