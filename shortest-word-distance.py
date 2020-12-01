class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        startIndex = []
        visit = set()
        moves = 0
        for index in range(len(words)):
            if words[index] == word1:
                startIndex.append(index)
                visit.add(index)
        while len(startIndex) > 0:
            moves += 1
            newAry = []
            for val in startIndex:
                if val + 1 != len(words):
                    if val + 1 not in visit:
                        if words[val+1] == word2:
                            return moves
                        newAry.append(val+1)
                        visit.add(val+1)
                    
                if val - 1 != -1:
                    if val - 1 not in visit:
                        if words[val-1] == word2:
                            return moves
                        newAry.append(val-1)
                        visit.add(val-1)
                
            startIndex = newAry
        return len(words)
        
        
