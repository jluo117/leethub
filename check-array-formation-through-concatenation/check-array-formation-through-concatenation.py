class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        table = set()
        for piece in pieces:
            curStr = ""
            for c in piece:
                curStr += str(c) + ','
            table.add(curStr)
        curCheck = ""
        for val in arr:
            curCheck += str(val)+','
            if curCheck in table:
                table.remove(curCheck)
                curCheck = ""
        return curCheck == ""
        
        
