class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        table = {}
        def helper(index):
            if index in table:
                return table[index]
            if index == len(days):
                return 0
            min_cost = float('inf')
            month_exp_day = days[index] +30
            for d in range(index,len(days)):
                if days[d] >= month_exp_day:
                    min_cost = min(min_cost,helper(d)+costs[2])
                    break
                if d == len(days) -1:
                    min_cost = min(min_cost,costs[2])
            week_exp_day = days[index]+7
            for d in range(index,len(days)):
                if days[d] >= week_exp_day:
                    min_cost = min(min_cost,helper(d)+costs[1])
                    break
                if d == len(days)-1:
                    min_cost = min(min_cost,costs[1])
            min_cost = min(min_cost,helper(index+1)+costs[0])
            table[index] = min_cost
            return table[index]
        return helper(0)
            