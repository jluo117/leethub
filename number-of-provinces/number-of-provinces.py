class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        claimed = set()
        count = 0
        
        def helper(curNode):
            if curNode in claimed:
                return
            claimed.add(curNode)
            nodeConnections = isConnected[curNode]
            for node in range(len(nodeConnections)):
                if nodeConnections[node] == 1:
                    helper(node)
            return
        for index in range(len(isConnected)):
            if index not in claimed:
                helper(index)
                count += 1
        return count
            
            
        