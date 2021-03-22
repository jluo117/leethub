class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacificSet = set()
        def pacificHelper(cord):
            if cord in pacificSet:
                return
            y,x = cord
            pacificSet.add(cord)
            if y > 0:
                if matrix[y][x] <= matrix[y-1][x]:
                    pacificHelper((y-1,x))
            if y < len(matrix)-1:
                if matrix[y][x] <= matrix[y+1][x]:
                    pacificHelper((y+1,x))
            if x > 0:
                if matrix[y][x] <= matrix[y][x-1]:
                    pacificHelper((y,x-1))
            if x < len(matrix[y])-1:
                if matrix[y][x] <= matrix[y][x+1]:
                    pacificHelper((y,x+1))
        atlanticSet = set()
        def atlanticHelper(cord):
            if cord in atlanticSet:
                return
            y,x = cord
            atlanticSet.add(cord)
            if y > 0:
                if matrix[y][x] <= matrix[y-1][x]:
                    atlanticHelper((y-1,x))
            if y < len(matrix)-1:
                if matrix[y][x] <= matrix[y+1][x]:
                    atlanticHelper((y+1,x))
            if x > 0:
                if matrix[y][x] <= matrix[y][x-1]:
                    atlanticHelper((y,x-1))
            if x < len(matrix[y])-1:
                if matrix[y][x] <= matrix[y][x+1]:
                    atlanticHelper((y,x+1))
        if len(matrix) == 0:
            return []
        for x in range(len(matrix[0])):
            pacificHelper((0,x))
        for y in range(len(matrix)):
            pacificHelper((y,0))
        for x in range(len(matrix[-1])):
            atlanticHelper((len(matrix)-1,x))
        for y in range(len(matrix)):
            atlanticHelper((y,len(matrix[y])-1))
        res = []
        for val in pacificSet:
            if val in atlanticSet:
                res.append(val)
        return res
                
        