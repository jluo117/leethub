class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        fails = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if col < len(grid[row])-1 and grid[row][col] == 1 and grid[row][col+1] == -1:
                    fails.add((row,col))
                if grid[row][col] == -1 and grid[row][col-1] == 1:
                    fails.add((row,col))
        alive = [i for i in range(len(grid[0]))]
        row = 0
        while row < len(grid):
            newSet = []
            for a in alive:
                if a == -1:
                    newSet.append(-1)
                    continue
                if a == -1:
                    newSet.append(-1)
                    continue
                if a == len(grid[row]):
                    newSet.append(-1)
                    continue
                if (row,a) not in fails:
                    if grid[row][a] == -1:
                        if a-1 == -1:
                            newSet.append(-1)
                            continue
                        newSet.append(a-1)
                    else:
                        if a + 1 == len(grid[row]):
                            newSet.append(-1)
                            continue
                        newSet.append(a+1)
                else:
                    newSet.append(-1)
        
            alive = newSet
            row += 1
        return alive
        