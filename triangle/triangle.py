class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        table = {}
        def helper(row,index):
            if row == len(triangle):
                return 0
            if (row,index) in table:
                return table[(row,index)]
            res = min(helper(row+1,index),helper(row+1,index+1)) + triangle[row][index]
            table[(row,index)] = res
            return res
        return helper(0,0)