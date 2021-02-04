class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        removeIndex = set()
        minAry = deque()
        maxAry = deque()
        maxLen = 0
        L = 0
        R = 0
        while R < len(nums):
            while len(minAry) > 0 and minAry[-1][0] > nums[R]:
                minAry.pop()
            minAry.append((nums[R],R))
            while len(maxAry) > 0 and maxAry[-1][0] < nums[R]:
                maxAry.pop()
            maxAry.append((nums[R],R))
            while maxAry[0][0] - minAry[0][0] > limit:
                removeIndex.add(L)
                while minAry[0][1] in removeIndex:
                    minAry.popleft()
                while maxAry[0][1] in removeIndex:
                    maxAry.popleft()
                L += 1
            
            maxLen = max(maxLen,(R-L)+1)
            R += 1
        return maxLen
                
                
                    
                    
        