class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        table = []
        for _ in range(len(text1)):
            a = []
            for _ in range(len(text2)):
                a.append(0)
            table.append(a)
        for index in range(len(text1)):
            t1_val = text1[index]
            for t2_index in range(len(text2)):
                max_val = 0
                if index > 0:
                    max_val = max(max_val, table[index-1][t2_index])
                if t2_index > 0:
                    max_val = max(max_val,table[index][t2_index-1])
                
                if text1[index] == text2[t2_index]:
                    if t2_index > 0 and index > 0:
                        max_val = max(max_val,table[index-1][t2_index-1]+1)
                    else:
                        max_val = max(max_val,1)
                table[index][t2_index] = max_val
        return table[len(text1)-1][len(text2)-1]
                        