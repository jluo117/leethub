class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        #2 = Justdead
        #3 = new
        for rowIndex in range(len(board)):
            for colIndex in range(len(board[rowIndex])):
                neigh = 0
                if rowIndex > 0:
                    if board[rowIndex-1][colIndex] == 2 or board[rowIndex-1][colIndex] == 1:
                        neigh += 1
                if rowIndex < len(board) -1:
                    if board[rowIndex+1][colIndex] == 2 or board[rowIndex+1][colIndex] == 1:
                        neigh += 1
                if colIndex > 0:
                    if board[rowIndex][colIndex-1] == 2 or board[rowIndex][colIndex-1] == 1:
                        neigh += 1
                if colIndex < len(board[rowIndex]) - 1:
                    if board[rowIndex][colIndex+1] == 2 or board[rowIndex][colIndex+1] == 1:
                        neigh += 1
                if rowIndex > 0 and colIndex > 0:
                    if board[rowIndex-1][colIndex-1] == 2 or board[rowIndex-1][colIndex-1] == 1:
                        neigh += 1
                if rowIndex > 0 and colIndex < len(board[rowIndex]) -1:
                    if board[rowIndex-1][colIndex+1] == 2 or board[rowIndex-1][colIndex+1] == 1:
                        neigh += 1
                if rowIndex < len(board) -1 and colIndex > 0:
                    if board[rowIndex+1][colIndex-1] == 2 or board[rowIndex+1][colIndex-1] == 1:
                        neigh += 1
                if rowIndex < len(board) -1 and colIndex < len(board[rowIndex]) -1:
                    if board[rowIndex+1][colIndex+1] == 2 or board[rowIndex+1][colIndex+1] == 1:
                        neigh += 1
                if board[rowIndex][colIndex] == 1:
                    if neigh < 2:
                        board[rowIndex][colIndex] = 2
                    if neigh > 3:
                        board[rowIndex][colIndex] = 2
                else:
                    if neigh == 3:
                        board[rowIndex][colIndex] = 3
        for rowIndex in range(len(board)):
            for colIndex in range(len(board[rowIndex])):
                if board[rowIndex][colIndex] == 2:
                    board[rowIndex][colIndex] = 0
                elif board[rowIndex][colIndex] == 3:
                    board[rowIndex][colIndex] = 1
        """
        Do not return anything, modify board in-place instead.
        """
        
