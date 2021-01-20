class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        numIslands = 0
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    isIsland = [True]
                    self.search(i, j, grid, isIsland)
                    if isIsland[0]:
                        numIslands += 1
    
        return numIslands
    
    
    def search(self, i, j, grid, isIsland):
    # out of bounds or not even a 0 anymore
        if i < 0 or j < 0 or i > len(grid) or j > len(grid[i]) or grid[i][j] == 1:
            return
    
    # if you are on the perimeter and you have a 0, then you cannot be surrounded by 1s, therefore stop
        if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1 and grid[i][j] == 0:
            isIsland[0] = False
            return
    
        grid[i][j] = 1
    
        self.search(i + 1, j, grid, isIsland)
        self.search(i - 1, j, grid, isIsland)
        self.search(i, j + 1, grid, isIsland)
        self.search(i, j - 1, grid, isIsland)
