class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0
        def helper(y,x):
            nodes = [(y,x)]
            curSize = 1
            grid[y][x] = 0
            while len(nodes):
                y,x = nodes.pop()
                if y > 0:
                    if grid[y-1][x] == 1:
                        grid[y-1][x] = 0
                        curSize += 1
                        nodes.append((y-1,x))
                if y < len(grid)-1:
                    if grid[y+1][x] == 1:
                        grid[y+1][x] = 0
                        curSize += 1
                        nodes.append((y+1,x))
                if x > 0:
                    if grid[y][x-1] == 1:
                        grid[y][x-1] = 0
                        curSize += 1
                        nodes.append((y,x-1))
                if x < len(grid[y])-1:
                    if grid[y][x+1] == 1:
                        grid[y][x+1] = 0
                        curSize += 1
                        nodes.append((y,x+1))
            return curSize
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    maxSize = max(maxSize,helper(y,x))
        return maxSize