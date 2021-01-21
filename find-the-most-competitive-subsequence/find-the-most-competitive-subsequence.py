class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        delRemain = len(nums) - k
        myOrder =deque()
        for num in nums:
            while len(myOrder) > 0 and myOrder[-1] > num and delRemain > 0:
                myOrder.pop()
                delRemain -= 1
            myOrder.append(num)
        res = []
        for num in myOrder:
            if len(res) < k:
                res.append(num)
        return res
        
