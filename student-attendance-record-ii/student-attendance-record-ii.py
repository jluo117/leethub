import numpy as np

class Solution(object):
    def checkRecord(self, n):
        A = np.matrix([
            [1, 1, 1, 0, 0, 0],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
        ])
        power = A
        mod = 10**9 + 7
        while n:
            if n & 1: power = (power * A) % mod
            A = A**2 % mod
            n >>= 1
        return power[3, 0]