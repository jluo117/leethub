class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        self.index = 0
        table = {}
        def helper():
            curId = int(logs[self.index].split(":")[0])
            if self.index == len(logs):
                return
            runtime = 0
            startTime = int(logs[self.index].split(":")[2])
            self.index += 1
            while self.index < len(logs):
                if logs[self.index].split(":")[1] == "start":
                    runtime += int(logs[self.index].split(":")[2]) - startTime
                    helper()
                    startTime = int(logs[self.index].split(":")[2])+1
                    self.index += 1
                else:
                    runtime += int(logs[self.index].split(":")[2]) - startTime+1
                    if curId in table:
                        table[curId] += runtime
                    else:
                        table[curId] = runtime
                    return
        while self.index < len(logs):
            helper()
        res = []
        for i in range(n):
            res.append(table[i])
        return res
            
                