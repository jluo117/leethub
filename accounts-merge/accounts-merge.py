class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        nameBucket = {}
        for account in accounts:
            if account[0] not in nameBucket:
                nameBucket[account[0]] = []
            setVal = set(account[1:])
            nameBucket[account[0]].append(setVal)
        def mergeBucket(name):
            finalBuckets = []
            bucket = nameBucket[name]
            merged = set()
            for index in range(len(bucket)):
                if index in merged:
                    continue
                merged.add(index)
                waiting = []
                newBucket = set()
                for val in bucket[index]:
                    waiting.append(val)
                    newBucket.add(val)
                while waiting:
                    popVal = waiting.pop()
                    for index in range(len(bucket)):
                        if index in merged:
                            continue
                        if popVal in bucket[index]:
                            merged.add(index)
                            for val in bucket[index]:
                                if val not in newBucket:
                                    newBucket.add(val)
                                    waiting.append(val)
                res = []
                for val in newBucket:
                    res.append(val)
                res.sort()
                finalBuckets.append(res)
            return finalBuckets
        res = []
        for val in nameBucket:
            bucketRes = mergeBucket(val)
            for bucket in bucketRes:
                res.append([val] + bucket)
        return res
                        
            
            
            
                
        
