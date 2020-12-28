class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = {}
        for road in roads:
            if road[0] in graph:
                graph[road[0]].append(road[1])
            else:
                graph[road[0]] = [road[1]]
            if road[1] in graph:
                graph[road[1]].append(road[0])
            else:
                graph[road[1]] = [road[0]]
        table = {}
        def helper(curNode,pathIndex):
            if pathIndex == len(targetPath):
                return 0,[]
            if (curNode,pathIndex) in table:
                return table[(curNode,pathIndex)]
            posMoves = graph[curNode]
            res = float('inf')
            curMove = []
            for move in posMoves:
                neededMoves,path = helper(move,pathIndex+1)
                if neededMoves < res:
                    curMove = path
                    res = neededMoves
            if names[curNode] != targetPath[pathIndex]:
                res += 1
            curMove = [curNode] + curMove
            table[(curNode,pathIndex)] = (res,curMove)
            return res,curMove
        res = float('inf')
        correctMove = []
        for s in graph:
            neededMoves,path = helper(s,0)
            if neededMoves < res:
                correctMove = path
                res = neededMoves
        
        
        return correctMove
