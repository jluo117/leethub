class Solution:
    def mySqrt(self, x: int) -> int:
        L = 1
        R = x
        while L <= R:
            
            mid_point = (L+R) // 2
            if mid_point * mid_point == x:
                return mid_point
            if mid_point * mid_point < x:
                L = mid_point + 1
            else:
                R = mid_point - 1
        return R
        