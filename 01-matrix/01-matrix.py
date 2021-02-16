class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        order = []
        moves = 0
        visit = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    order.append((row,col))
                    visit.add((row,col))
        while len(order):
            newOrder = []
            moves += 1
            for step in order:
                x = step[1]
                y = step[0]
                if x > 0:
                    if (y,x-1) not in visit:
                        visit.add((y,x-1))
                        matrix[y][x-1] = moves
                        newOrder.append((y,x-1))
                if x < len(matrix[y])-1:
                    if (y,x+1) not in visit:
                        visit.add((y,x+1))
                        matrix[y][x+1] = moves
                        newOrder.append((y,x+1))
                if y > 0:
                    if (y-1,x) not in visit:
                        visit.add((y-1,x))
                        matrix[y-1][x] = moves
                        newOrder.append((y-1,x))
                if y < len(matrix)-1:
                    if (y+1,x) not in visit:
                        visit.add((y+1,x))
                        matrix[y+1][x] = moves
                        newOrder.append((y+1,x))
            order = newOrder
        return matrix
                