class Solution:
    def hIndex(self, citations: List[int]) -> int:
        table = Counter()
        for cite in citations:
            if cite > len(citations):
                table[len(citations)] += 1
            else:
                table[cite] += 1
        running = 0
        
        for i in range(len(citations),0,-1):
            if table[i] + running  >= i:
                return i
            running += table[i]
        return 0
        