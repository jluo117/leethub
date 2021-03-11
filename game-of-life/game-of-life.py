'''
2 new cell
-1 die cell
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def neighborCount(y,x):
            count = 0
            if y > 0:
                if board[y-1][x] == 1 or board[y-1][x] == -1:
                    count += 1
            if x > 0:
                if board[y][x-1] == 1 or board[y][x-1] == -1:
                    count += 1
            if y> 0 and x > 0:
                if board[y-1][x-1] == 1 or board[y-1][x-1] == -1:
                    count += 1
            if y > 0 and x < len(board[y])-1:
                if board[y-1][x+1] == 1 or board[y-1][x+1] == -1:
                    count += 1
            if y < len(board)-1 and x > 0:
                if board[y+1][x-1] == 1 or board[y+1][x-1] == -1:
                    count += 1
            if y < len(board)-1:
                if board[y+1][x] == 1 or board[y+1][x] == -1:
                    count += 1
            if x < len(board[y])-1:
                if board[y][x+1] == 1 or board[y][x+1] == -1:
                    count += 1
            if y < len(board)-1 and x < len(board[y])-1:
                if board[y+1][x+1] == 1 or board[y+1][x+1] == -1:
                    count += 1
            return count
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0:
                    if neighborCount(y,x) == 3:
                        board[y][x] = 2
                else:
                    if 2 > neighborCount(y,x)  or neighborCount(y,x) > 3:
                        board[y][x] = -1
        
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == -1:
                    board[y][x] = 0
                if board[y][x] == 2:
                    board[y][x] = 1
        
        """
        Do not return anything, modify board in-place instead.
        """
        