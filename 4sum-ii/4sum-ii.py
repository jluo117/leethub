class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        CDTable = {}
        for val in C:
            for dVal in D:
                tol = val + dVal
                if tol in CDTable:
                    CDTable[tol] += 1
                else:
                    CDTable[tol] = 1
        res = 0
        for val in A:
            for bVal in B:
                tol = val + bVal
                if -tol in CDTable:
                    res += CDTable[-tol]
        return res
