class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        self.index = 0
        self.curTime = 0
        table = {}
        def helper():
            tolRunTime = 0
            logSplit = logs[self.index].split(':')
            function = int(logSplit[0])
            startTime = int(logSplit[2])
            self.index += 1
                
            while self.index < len(logs):
                curLog = logs[self.index].split(':')
                if curLog[1] == "start":
                    tolRunTime += (int(curLog[2])-startTime)
                    helper()
                    startTime = int(logs[self.index].split(':')[2])+1
                    self.index += 1
                    continue
                if curLog[1] == "end":
                    tolRunTime += (int(curLog[2])-startTime)+1
                    
                    if function in table:
                        table[function] += tolRunTime
                    else:
                        table[function] = tolRunTime
                    return 
        while self.index < len(logs):
            helper()
            self.index += 1
        ary = []
        print(table)
        for v in range(n):
            ary.append(table[v])
        return ary
        