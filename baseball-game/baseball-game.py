class Solution:
    def calPoints(self, ops: List[str]) -> int:
        events = []
        for op in ops:
            if op == "+":
                events.append(events[-1] + events[-2])
            elif op == 'D':
                events.append(events[-1] *2)
            elif op == 'C':
                events.pop()
            else:
                events.append(int(op))
        return sum(events)
