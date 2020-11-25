class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def helper(curWord):
            toMap = {}
            seen = set()
            if len(curWord) != len(pattern):
                return False
            for w,p in zip(curWord,pattern):
                
                if w in toMap:
                    if toMap[w] != p:
                        return False
                else:
                    if p in seen:
                        return False
                    toMap[w] = p
                    seen.add(p)
            
            return True
        res = []
        for word in words:
            if helper(word):
                res.append(word)
        return res
        
