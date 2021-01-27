class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['$'] = {}


    def search(self, word: str) -> bool:
        def helper(node,index):
            
            if index == len(word):
                if '$' in node:
                    return True
                else:
                    return False
            
            if word[index] == '.':
                for c in node:
                    if helper(node[c],index+1):
                        
                        return True
                return False
            else:
                if word[index] not in node:
                    return False
                node = node[word[index]]
                return helper(node,index+1)
        return helper(self.trie,0)
            