class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        takenClass = set()
        lockedClass = set()
        preReq = {}
        openers = {}
        def canTake(classNum):
            if classNum not in preReq:
                return True
            for needed in preReq[classNum]:
                if needed not in takenClass:
                    return False
            return True
        for relation in relations:
            lockedClass.add(relation[1])
            if relation[0] not in openers:
                openers[relation[0]] = [relation[1]]
            else:
                openers[relation[0]].append(relation[1])
            if relation[1] not in preReq:
                preReq[relation[1]] =[relation[0]]
            else:
                preReq[relation[1]].append(relation[0])
        order = []
        moves = 0
     
        if n == 0:
            return 0
        for classNum in range(1,n+1):
            if classNum not in lockedClass:
                order.append(classNum)
        
        while len(order):
            newOrder = []
            moves += 1
            for classNum in order:
                takenClass.add(classNum)
                if classNum in openers:
                    for pot in openers[classNum]:
                        if canTake(pot):
                            newOrder.append(pot)
            order = newOrder
        if len(takenClass) == n:
            return moves
        return -1
            
        