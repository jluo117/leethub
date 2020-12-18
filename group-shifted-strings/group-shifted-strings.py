class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        def wordDis(prev,cur):
            startPos = ord(prev) - 97
            shift = 0
            while chars[startPos] != cur:
                startPos += 1
                if startPos == len(chars):
                    startPos = 0
                shift += 1
            return shift
        table = {}
        for string in strings:
            curstr = "0"
            for w in range(1,len(string)):
                curstr += str(wordDis(string[w-1],string[w]))
            if curstr in table:
                table[curstr].append(string)
            else:
                table[curstr] = [string]
        res = []
        for val in table:
            res.append(table[val])
        print(table)
