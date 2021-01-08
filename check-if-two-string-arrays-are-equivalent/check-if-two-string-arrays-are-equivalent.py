class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        aIndex = 0
        aWord = 0
        bIndex = 0
        bWord = 0
        while aIndex < len(word1) and bIndex < len(word2):
            if word1[aIndex][aWord] != word2[bIndex][bWord]:
                print("no match")
                return False
            aWord += 1
            bWord += 1
            if aWord == len(word1[aIndex]):
                aWord = 0
                aIndex += 1
            if bWord == len(word2[bIndex]):
                bWord = 0
                bIndex += 1
        
        if aIndex != len(word1) or bIndex != len(word2):
            return False
        return True
