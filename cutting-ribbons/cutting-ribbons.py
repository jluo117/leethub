class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_cut(size):
            if size == 0:
                return True
            count = 0
            for r in ribbons:
                if r < size:
                    continue
                count += r//size
            return count >= k
        upper = max(ribbons)
        min_val = 0
        last_pos = 0
        while min_val <= upper:
            mid_point = (min_val + upper) //2
            if can_cut(mid_point):
                last_pos = mid_point
                min_val = mid_point + 1
            else:
                upper = mid_point -1
        return last_pos
                
                
        