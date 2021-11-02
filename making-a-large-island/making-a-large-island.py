class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    grid[row][col] = -1
        size_table = {}
        def mark_size(marker,start_pos):
            order = [start_pos]
            count = 1
            y,x = start_pos
            grid[y][x] = marker
            while len(order):
                new_group = []
                for pos in order:
                    y,x = pos
                    if y < len(grid)-1:
                        if grid[y+1][x] == -1:
                            new_group.append((y+1,x))
                            count += 1
                            grid[y+1][x] = marker
                    if y > 0:
                        if grid[y-1][x] == -1:
                            new_group.append((y-1,x))
                            count += 1
                            grid[y-1][x] = marker
                    if x < len(grid[y])-1:
                        if grid[y][x+1] == -1:
                            new_group.append((y,x+1))
                            count += 1
                            grid[y][x+1] = marker
                    if x > 0:
                        if grid[y][x-1] == -1:
                            new_group.append((y,x-1))
                            count += 1
                            grid[y][x-1] = marker
                order = new_group
            return count
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == -1:
                    mark = len(size_table)+1
                    size_table[mark] = mark_size(mark,(row,col))
        if len(size_table) == 0:
            return 1
        max_val = max([size_table[val] for val in size_table])
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    merge_val = set()
                    if row < len(grid)-1:
                        if grid[row+1][col] != 0:
                            merge_val.add(grid[row+1][col])
                    if row > 0:
                        if grid[row-1][col] != 0:
                            merge_val.add(grid[row-1][col])
                    if col < len(grid[row])-1:
                        if grid[row][col+1] != 0:
                            merge_val.add(grid[row][col+1])
                    if col > 0:
                        if grid[row][col-1] != 0:
                            merge_val.add(grid[row][col-1])
                    sub_sum = 1
                    for val in merge_val:
                        sub_sum += size_table[val]
                    max_val = max(max_val,sub_sum)
        return max_val
        
                        
                            