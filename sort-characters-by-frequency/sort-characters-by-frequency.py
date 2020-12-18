class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        myHeap = []
        for val in freq:
            myHeap.append((-freq[val],val))
        heapify(myHeap)
        res = ""
        while len(myHeap) > 0:
            popVal = (heappop(myHeap))
            res += popVal[1] * -popVal[0] 
        return res
        
