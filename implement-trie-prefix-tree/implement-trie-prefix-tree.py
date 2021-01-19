class Trie:
​
    def __init__(self):
        self.myTrie = [{},False]
        """
        Initialize your data structure here.
        """
        
​
    def insert(self, word: str) -> None:
        curLayer= self.myTrie
        for c in word:
            if c not in curLayer[0]:
                curLayer[0][c] = [{},False]
                curLayer = curLayer[0][c]
            else:
                curLayer = curLayer[0][c]
        curLayer[1] = True
        
        """
        Inserts a word into the trie.
        """
        
​
    def search(self, word: str) -> bool:
        curLayer = self.myTrie
        for c in word:
            if c not in curLayer[0]:
                return False
            else:
                curLayer = curLayer[0][c]
        return curLayer[1]
        """
        Returns if the word is in the trie.
        """
        
​
    def startsWith(self, prefix: str) -> bool:
        curLayer = self.myTrie
        for c in prefix:
