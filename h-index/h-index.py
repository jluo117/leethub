'''
0 1 3 5 6
1
2
3
'''
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citationCount = collections.Counter()
        count = 0
        for cite in citations:
            if cite > len(citations):
                citationCount[len(citations)] += 1
            else:
                citationCount[cite] += 1
        
        running = 0
        for index in range(len(citations),-1,-1):
            if index in citationCount:
                running += citationCount[index]
            if running >= index:
                return index
        return 0
            
        
            
        
        
        
        