class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(index,cord,used):
            if index == len(word):
                
                return True
            x = cord[1]
            y = cord[0]
           
            if x > 0:
                if board[y][x-1] == word[index] and (y,x-1) not in used:
                    used.add((y,x-1))
                    if helper(index+1,(y,x-1),used):
                        return True
                    used.remove((y,x-1))
            if x < len(board[y])-1:
                if board[y][x+1] == word[index] and (y,x+1) not in used:
                    used.add((y,x+1))
                    if helper(index+1,(y,x+1),used):
                        return True
                    used.remove((y,x+1))
            if y > 0:
                if board[y-1][x] == word[index] and (y-1,x) not in used:
                    used.add((y-1,x))
                    if helper(index+1,(y-1,x),used):
                        return True
                    used.remove((y-1,x))
            if y < len(board)-1:
                if board[y+1][x] == word[index] and (y+1,x) not in used:
                    used.add((y+1,x))
                    if helper(index+1,(y+1,x),used):
                        return True
                    used.remove((y+1,x))
            return False
        used = set()
        for y in range(len(board)):
            for x in range(len(board[y])):
                if word[0] == board[y][x]:
                    used.add((y,x))
                    if helper(1,(y,x),used):
                        return True
                    used.remove((y,x))
        return False
                
        
