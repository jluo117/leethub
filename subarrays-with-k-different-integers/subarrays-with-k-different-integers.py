'''
111112
L    L2


'''
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        mainWindow = {}
        secWindow = {}
        L = 0
        L2 = 0
        R = 0
        tol = 0
        while R < len(A):
            if A[R] in mainWindow:
                mainWindow[A[R]] += 1
            else:
                mainWindow[A[R]] = 1
            if A[R] not in secWindow:
                secWindow[A[R]] = 1
            else:
                secWindow[A[R]] += 1
            while len(mainWindow) > K:
                mainWindow[A[L]] -= 1
                if mainWindow[A[L]] == 0:
                    del mainWindow[A[L]]
                L += 1
            while len(secWindow) >= K:
                secWindow[A[L2]] -= 1
                if secWindow[A[L2]] == 0:
                    del secWindow[A[L2]]
                L2 += 1
            tol += L2 - L
            R += 1
        return tol
        