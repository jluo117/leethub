class WordDistance:
​
    def __init__(self, words: List[str]):
        self.table = {}
        for index in range(len(words)):
            if words[index] in self.table:
                self.table[words[index]].append(index)
            else:
                self.table[words[index]] = [index]
        
        
​
    def shortest(self, word1: str, word2: str) -> int:
        word1Table = self.table[word1]
        word2Table = self.table[word2]
        minDis = float('inf')
        for sIndex in word1Table:
            for index in word2Table:
                minDis = min(minDis,abs(index-sIndex))
        return minDis
​
​
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
