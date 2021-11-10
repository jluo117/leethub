class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set()
        for word in wordDict:
            word_set.add(word)
        table = {}
        def helper(index):
            if index in table:
                return table[index]
            if index == len(s):
                return True
            cur_str = ""
            for c_index in range(index,len(s)):
                cur_str += s[c_index]
                
                if cur_str in word_set:
                    if helper(c_index+1):
                        table[index] = True
                        return True
            table[index] = False
            return False
        return helper(0)