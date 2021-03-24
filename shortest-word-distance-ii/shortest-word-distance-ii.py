class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.graph = {}
        for index in range(len(wordsDict)):
            if wordsDict[index] not in self.graph:
                self.graph[wordsDict[index]] = [index]
            else:
                self.graph[wordsDict[index]].append(index)
            
        
                    

    def shortest(self, word1: str, word2: str) -> int:
        word1Index = self.graph[word1]
        word2Index = self.graph[word2]
        minVal = float('inf')
        for val in word1Index:
            for lowerVal in word2Index:
                minVal =min(minVal,abs(val-lowerVal))
        return minVal
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)