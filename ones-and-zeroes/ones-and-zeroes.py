class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        strTable = []
        for s in strs:
            table = {'0':0,'1':0}
            for c in s:
                table[c] += 1
            strTable.append(table)
        dp = {}
        def helper(index,m,n):
            if index == len(strTable):
                return 0
            if (index,m,n) in dp:
                return dp[index,m,n]
            curTable = strTable[index]
            res = 0
            if curTable['0'] <= m and curTable['1'] <= n:
                res = helper(index+1,m-curTable['0'],n-curTable['1'])+1
            res = max(res,helper(index+1,m,n))
            dp[(index,m,n)] = res
            return res
        return helper(0,m,n)