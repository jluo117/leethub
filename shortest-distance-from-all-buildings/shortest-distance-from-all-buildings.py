class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        startCord = []
        badPos = []
        for y in range(0,len(grid)):
            for x in range(0,len(grid[y])):
                if grid[y][x] == 1:
                    startCord.append((y,x))
                if grid[y][x] == 2:
                    badPos.append((y,x))
        self.masterGrid = []
        if len(startCord) == len(grid) * len(grid[0]):
            return -1
        for y in range(0,len(grid)):
            newGrid = []
            for x in range(0,len(grid[y])):
                newGrid.append([float('inf'),0])
            self.masterGrid.append(newGrid)
        
        def helper(startLoc):
            visit = set()
            moves = [startLoc]
            visit.add(startLoc)
            curMoves = 0
            while len(moves) > 0:
                curMoves += 1
                newMoves = []
                for move in moves:
                
                    y = move[0]
                    x = move[1]
                   
                    if y > 0:
                        if grid[y-1][x] != 2 and (y-1,x) not in visit and grid[y-1][x] != 1:
                            newMoves.append((y-1,x))
                            visit.add((y-1,x))
                            if self.masterGrid[y-1][x][0] == float('inf'):
                                self.masterGrid[y-1][x][0] = 0
                            self.masterGrid[y-1][x][0] += curMoves
                            self.masterGrid[y-1][x][1] += 1
                    if y < len(grid)-1:
                        if grid[y+1][x] != 2 and (y+1,x) not in visit and grid[y+1][x] != 1:
                            newMoves.append((y+1,x))
                            visit.add((y+1,x))
                            if self.masterGrid[y+1][x][0] == float('inf'):
                                self.masterGrid[y+1][x][0] = 0
                            self.masterGrid[y+1][x][0] += curMoves
                            self.masterGrid[y+1][x][1] += 1
                    if x > 0:
                        if grid[y][x-1] != 2 and (y,x-1) not in visit and grid[y][x-1] != 1:
                            newMoves.append((y,x-1))
                            visit.add((y,x-1))
                            if self.masterGrid[y][x-1][0] == float('inf'):
                                self.masterGrid[y][x-1][0] = 0
                            self.masterGrid[y][x-1][0] += curMoves
                            self.masterGrid[y][x-1][1] += 1
                    if x < len(grid[y]) -1:
                        if grid[y][x+1] != 2 and (y,x+1) not in visit and grid[y][x+1] != 1:
                            newMoves.append((y,x+1))
                            visit.add((y,x+1))
                            if self.masterGrid[y][x+1][0] == float('inf'):
                                self.masterGrid[y][x+1][0] = 0
                            self.masterGrid[y][x+1][0] += curMoves
                            self.masterGrid[y][x+1][1] += 1
                 
                moves = newMoves
        for cord in startCord:
            
            helper(cord)
        
        minVal = float('inf')
        for y in range(0,len(grid)):
            for x in range(0,len(grid[y])):
                if grid[y][x] == 1:
                    continue
                if self.masterGrid[y][x][0] == float('inf'):
                    continue
                if self.masterGrid[y][x][1] != len(startCord):
                    continue
                minVal = min(self.masterGrid[y][x][0],minVal)
        if minVal == float('inf'):
            return -1
        return minVal
        