'''
abcde
Sindex
acd
​
'''
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        Stable = {}
        for index in range(len(S)):
            c = S[index]
            if c not in Stable:
                Stable[c] = [index]
            else:
                Stable[c].append(index)
        def isMatch(word):
            tableIndex = {}
            for val in Stable:
                tableIndex[val] = 0
            curIndex = 0
            
            
            for c in word:
                if c not in tableIndex:
                    return False
                while Stable[c][tableIndex[c]] < curIndex:
                    tableIndex[c] += 1
                    if tableIndex[c] == len(Stable[c]):
                        return False
                curIndex = Stable[c][tableIndex[c]] + 1
            return True
        res = 0
        for word in words:
            res += isMatch(word)
        return res
            
