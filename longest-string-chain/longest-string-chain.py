class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        table = {}
        for word in words:
            if len(word) in table:
                table[len(word)].append(word)
            else:
                table[len(word)] = [word]
        def isChain(sourceWord,targetWord):
            dif = False
            sIndex = 0
            tIndex = 0
            while sIndex < len(sourceWord):
                if sourceWord[sIndex] != targetWord[tIndex]:
                    if dif:
                        return False
                    dif = True
                    tIndex += 1
                    continue
                sIndex += 1
                tIndex += 1
            if tIndex < len(targetWord):
                if dif:
                    return False
                return True
            return True
                    
            
        dp = {}
        def helper(word):
            if word in dp:
                return dp[word]
            if len(word)+1 not in table:
                return 1
            maxVal = 1
            for posWord in table[len(word)+1]:
                if isChain(word,posWord):
                    
                    maxVal = max(maxVal,helper(posWord)+1)
            dp[word] = maxVal
            return maxVal
        maxVal = 0
        for word in words:
            maxVal = max(maxVal,helper(word))
        return maxVal