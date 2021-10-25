class MinStack:

    def __init__(self):
        self.min_stk = []
        self.cur_stk = []

    def push(self, val: int) -> None:
        if len(self.min_stk) == 0:
            self.min_stk.append(val)
        elif self.min_stk[-1] >= val:
            self.min_stk.append(val)
        self.cur_stk.append(val)

    def pop(self) -> None:
        if len(self.cur_stk) == 0:
            return
        pop_val = self.cur_stk.pop()
        if pop_val == self.min_stk[-1]:
            self.min_stk.pop()
        

    def top(self) -> int:
        if len(self.cur_stk):
            return self.cur_stk[-1]

    def getMin(self) -> int:
        if len(self.min_stk):
            return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()