class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        if grid[0][0] == 1:
            return -1
        r = len(grid) -1
        c = len(grid[r])-1
        if len(grid) == 1 and len(grid[0]) == 1:
            return 1
        visit = {(0,0)}
        moves = 1
        order = [(0,0)]
        while len(order):
            moves += 1
            newOrder = []
            for m in order:
                y = m[0]
                x = m[1]
                if y > 0:
                    if grid[y-1][x] == 0 and (y-1,x) not in visit:
                        newOrder.append((y-1,x))
                        visit.add((y-1,x))
                        if (y-1,x) ==(r,c):
                            return moves
                if y < r:
                    if grid[y+1][x] == 0 and (y+1,x) not in visit:
                        newOrder.append((y+1,x))
                        visit.add((y+1,x))
                        if (y+1,x) == (r,c):
                            return moves
                if x > 0:
                    if grid[y][x-1] == 0 and (y,x-1) not in visit:
                        newOrder.append((y,x-1))
                        visit.add((y,x-1))
                        if (y,x-1) == (r,c):
                            return moves
                if x < c:
                    if grid[y][x+1] == 0 and (y,x+1) not in visit:
                        newOrder.append((y,x+1))
                        visit.add((y,x+1))
                        if (y,x+1) == (r,c):
                            return moves
                if y > 0 and x > 0:
                    if grid[y-1][x-1] == 0 and (y-1,x-1) not in visit:
                        newOrder.append((y-1,x-1))
                        visit.add((y-1,x-1))
                        if (y-1,x-1) == (r,c):
                            return moves
                if y > 0 and x < c:
                    if grid[y-1][x+1] == 0 and (y-1,x+1) not in visit:
                        newOrder.append((y-1,x+1))
                        visit.add((y-1,x+1))
                        if (y-1,x+1) == (r,c):
                            return moves
                if y < r and x > 0:
                    if grid[y+1][x-1] == 0 and (y+1,x-1) not in visit:
                        newOrder.append((y+1,x-1))
                        visit.add((y+1,x-1))
                        if (y+1,x-1) == (r,c):
                            return moves
                if y < r and x < c:
                    if grid[y+1][x+1] == 0 and (y+1,x+1) not in visit:
                        newOrder.append((y+1,x+1))
                        visit.add((y+1,x+1))
                        if (y+1,x+1) == (r,c):
                            return moves
            order = newOrder
        return -1
        
        