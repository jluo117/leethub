class MedianFinder:

    def __init__(self):
        self.myStream = []
        """
        initialize your data structure here.
        """
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.myStream,num)
        

    def findMedian(self) -> float:
        if len(self.myStream) % 2 == 0:
            return (int(self.myStream[len(self.myStream)//2]) + int(self.myStream[(len(self.myStream)//2)-1]) )/2
        else:
            return self.myStream[len(self.myStream)//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()