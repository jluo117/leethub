class Solution:

    def __init__(self, w: List[int]):
        self.curSum = 0
        self.res = []
        
        for index in range(len(w)):
            self.curSum += w[index]
            self.res.append(self.curSum)

    def pickIndex(self) -> int:
        target = randrange(self.curSum)
        return bisect.bisect(self.res,target)
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()