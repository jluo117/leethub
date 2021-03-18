class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        redNode = set()
        greenNode = set()
        graph = {}
        def hasLoop(node):
            if node in greenNode:
                return True
            if node not in graph:
                return True
            if node in redNode:
                return False
            redNode.add(node)
            for childNode in graph[node]:
                if not hasLoop(childNode):
                    return False
            greenNode.add(node)
            return True
        for pre in (prerequisites):
            if pre[0] in graph:
                graph[pre[0]].append(pre[1])
            else:
                graph[pre[0]] = [pre[1]]
        for node in range(numCourses):
            if hasLoop(node) == False:
                return []
        takenClass = set()
        order = []
        def takeClass(node):
            
            if node in takenClass:
                return
            if node not in graph:
                order.append(node)
                takenClass.add(node)
                return
            for pre in graph[node]:
                takeClass(pre)
            takenClass.add(node)
            order.append(node)
        for curClass in range(numCourses):
            takeClass(curClass)
        return order
            
        