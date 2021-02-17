class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        firstRow = set(r1)
        secondRow = set(r2)
        thirdRow = set(r3)
        def helper(row,word):
            
            for c in word:
                if c.lower() not in row:
                    return False
            return True
        res = []
        for word in words:
            
            if word[0].lower() in firstRow:
                if helper(firstRow,word):
                    res.append(word)
            if word[0].lower() in secondRow:
                if helper(secondRow,word):
                    res.append(word)
            if word[0].lower() in thirdRow:
                if helper(thirdRow,word):
                    res.append(word)
        return res
        