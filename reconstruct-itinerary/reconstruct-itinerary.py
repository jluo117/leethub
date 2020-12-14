class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        table = {}
        usedTable = {}
        for ticket in tickets:
            if ticket[0] not in table:
                table[ticket[0]] = []
                table[ticket[0]].append(ticket[1])
                usedTable[ticket[0]] = set()
            else:
                table[ticket[0]].append(ticket[1])
        for val in table:
            table[val].sort()
        self.res = None
        def helper(pos,used,route):
            if used == len(tickets) and self.res == None:
                self.res = route
            if pos not in table or table[pos] == []:
                return
            for index in range(len(table[pos])):
                if index in usedTable[pos]:
                    continue
                frontPop = table[pos][index]
                usedTable[pos].add(index)
                helper(frontPop,used+1,route + [frontPop])
                if self.res != None:
                    return
                usedTable[pos].remove(index)
        helper("JFK",0,["JFK"])
        return self.res
            
