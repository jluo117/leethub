class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        if n == 0:
            return []
        graph = {}
        visit = set()
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[1]].append(edge[0])
        res = {}
        def helper(node):
            visit.add(node)
            levelTable = {labels[node]:1}
            for edge in graph[node]:
                if edge in visit:
                    continue
                resultingEdge = helper(edge)
                for val in resultingEdge:
                    if val not in levelTable:
                        levelTable[val] = resultingEdge[val]
                    else:
                        levelTable[val] += resultingEdge[val]
            res[node] = levelTable[labels[node]]
            return levelTable
            
        
        for i in range(n):
            if i not in res:
                helper(i)
        resAry = []
        for i in range(n):
            resAry.append(res[i])
        return resAry
        