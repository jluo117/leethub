class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countWord(word):
            counter = collections.Counter(word)
            res = ""
            for i in range(ord('a'),ord('z')+1):
                if chr(i) in counter:
                    res += chr(i) + str(counter[chr(i)])
            return res
        table = {}
        for word in strs:
            cWord = countWord(word)
            if cWord in table:
                table[cWord].append(word)
            else:
                table[cWord] = [word]
        res = [table[val] for val in table]
        return res
            