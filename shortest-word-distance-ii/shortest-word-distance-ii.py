class WordDistance:

    def __init__(self, words: List[str]):
        self.table = {}
        for index in range(len(words)):
            if words[index] in self.table:
                self.table[words[index]].append(index)
            else:
                self.table[words[index]] = [index]
        
        

    def shortest(self, word1: str, word2: str) -> int:
        word1Table = self.table[word1]
        word2Table = self.table[word2]
        w1Index = 0
        w2Index = 0
        minDif = float('inf')
        while w1Index < len(word1Table) and w2Index < len(word2Table):
            minDif = min(minDif,abs(word1Table[w1Index]-word2Table[w2Index]))
            if word1Table[w1Index] < word2Table[w2Index]:
                w1Index += 1
            else:
                w2Index += 1
        return minDif


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)