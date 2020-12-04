class MyCalendar:
​
    def __init__(self):
        self.occupied = []
        
​
    def book(self, start: int, end: int) -> bool:
        for val in self.occupied:
            if val[0] < end and start < val[1]:
                return False
        bisect.insort(self.occupied,(start,end))
        return True
                
            
        
​
​
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
