class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.Counter(s)
        sortedFreq = []
        for val in freq:
            sortedFreq.append(freq[val])
        sortedFreq.sort()
        lastDrop = float('inf')
        moves = 0
        for val in reversed(sortedFreq):
            if val >= lastDrop:
                if lastDrop == 0:
                    moves += val
                    continue
                lastDrop = lastDrop-1
                moves += abs(val-lastDrop)
            else:
                lastDrop = val
        return moves
                
        
        