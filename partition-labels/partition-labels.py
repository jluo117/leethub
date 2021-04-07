class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        wordTable = {}
        for index in range(len(S)):
            wordTable[S[index]] = index
        L = 0
        maxCap = 0
        partitions = []
        for index in range(len(S)):
            maxCap = max(wordTable[S[index]],maxCap)
            if index == maxCap:
                partitions.append((maxCap-L)+1)
                maxCap = index +1
                L = index + 1
        return partitions
        