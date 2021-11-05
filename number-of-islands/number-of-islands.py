class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(cord):
            order = [cord]
            while len(order) > 0:
                newOrder = []
                for node in order:
                    x = node[1]
                    y = node[0]
                    if x > 0:
                        if grid[y][x-1] == '1':
                            grid[y][x-1] = '0'
                            newOrder.append((y,x-1))
                    if x < len(grid[y])-1:
                        if grid[y][x+1] == '1':
                            grid[y][x+1] = '0'
                            newOrder.append((y,x+1))
                    if y > 0:
                        if grid[y-1][x] == '1':
                            grid[y-1][x] = '0'
                            newOrder.append((y-1,x))
                    if y < len(grid)-1:
                        if grid[y+1][x] == '1':
                            grid[y+1][x] = '0'
                            newOrder.append((y+1,x))
                order = newOrder
        tolIsland = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    tolIsland += 1
                    helper((row,col))
        return tolIsland
        