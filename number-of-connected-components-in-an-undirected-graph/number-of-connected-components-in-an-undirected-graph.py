class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = {}
        for edge in edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
            if edge[1] in graph:
                graph[edge[1]].append(edge[0])
            else:
                graph[edge[1]] = [edge[0]]
        visit = set()
        def helper(curNode):
            if curNode in visit:
                return
            if curNode not in graph:
                return
            visit.add(curNode)
            for edge in graph[curNode]:
                helper(edge)
        for edge in range(n):
            if edge not in visit:
                helper(edge)
                count += 1
        return count
        