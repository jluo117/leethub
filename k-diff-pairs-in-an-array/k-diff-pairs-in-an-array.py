class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seenVals = set()
        res = set()
        for num in nums:
            
            if num-k in seenVals:
                res.add((num-k,num))
            if num+k in seenVals:
                res.add((num,num+k))
            seenVals.add(num)
        print(res)
        return len(res)
        
