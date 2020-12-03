class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        hasZero = False
        startOrder = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 0:
                    hasZero = True
                else:
                    startOrder.append((y,x))
        if hasZero == False:
            return -1
        if len(startOrder) == 0:
            return -1
        curMoves = 0
        while len(startOrder) > 0:
            newOrder = []
            curMoves += 1
            for move in startOrder:
                x = move[1]
                y= move[0]
                if x > 0:
                    if grid[y][x-1] == 0:
                        grid[y][x-1] = curMoves
                        newOrder.append((y,x-1))
                if y > 0:
                    if grid[y-1][x] == 0:
                        grid[y-1][x] = curMoves
                        newOrder.append((y-1,x))
                if x < len(grid[0])-1:
                    if grid[y][x+1] == 0:
                        grid[y][x+1] = curMoves
                        newOrder.append((y,x+1))
                if y < len(grid)-1:
                    if grid[y+1][x] == 0:
                        grid[y+1][x] = curMoves
                        newOrder.append((y+1,x))
            startOrder = newOrder
        maxDis = -1
        for row in grid:
            maxDis = max(max(row),maxDis)
        return maxDis
            
