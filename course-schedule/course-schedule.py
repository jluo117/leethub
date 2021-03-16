class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        redNodes = set()
        greenNodes = set()
        for pre in prerequisites:
            if pre[0] in graph:
                graph[pre[0]].append(pre[1])
            else:
                graph[pre[0]] = [pre[1]]
        def helper(node):
            if node in greenNodes:
                return True
            if node in redNodes:
                return False
            redNodes.add(node)
            if node not in graph:
                greenNodes.add(node)
                return True
            for child in graph[node]:
                if not helper(child):
                    return False
            greenNodes.add(node)
            return True
        for num in range(numCourses):
            if not helper(num):
                return False
        return True
        