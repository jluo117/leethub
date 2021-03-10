class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            charCount = collections.Counter()
            alpha = set()
            for c in string:
                charCount[c] += 1
                alpha.add(c)
            hashVal = ""
            listVal = list(alpha)
            listVal.sort()
            for val in listVal:
                hashVal += (val + str(charCount[val]))
            if hashVal in anagrams:
                anagrams[hashVal].append(string)
            else:
                anagrams[hashVal] = [string]
        
        return [anagrams[val] for val in anagrams]