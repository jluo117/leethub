class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        maxQueue = []
        score = [0]*len(nums)
        lastComputed = 0
        heapq.heappush(maxQueue,(-nums[0],0))
        score[0] = nums[0]
        for index in range(1,len(nums)):
            while len(maxQueue):
                if maxQueue[0][1] < index-k:
                    heapq.heappop(maxQueue)
                else:
                    break
            if len(maxQueue):
                trueVal = -maxQueue[0][0]
                trueVal += nums[index]
                score[index] = trueVal
                heapq.heappush(maxQueue,(-trueVal,index))
            else:
                trueVal = nums[index]
                heapq.heappush(maxQueue,(trueVal,index))
                lastComputed = trueVal
                score[index] = trueVal
        return score[-1]
                
                
            