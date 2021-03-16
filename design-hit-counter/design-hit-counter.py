class HitCounter:

    def __init__(self):
        self.events = deque()
        """
        Initialize your data structure here.
        """
        

    def hit(self, timestamp: int) -> None:
        self.events.append(timestamp)
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        

    def getHits(self, timestamp: int) -> int:
        while self.events and self.events[0] <= timestamp - 300:
            self.events.popleft()
        return len(self.events)
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)