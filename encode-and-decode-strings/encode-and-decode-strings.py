class Codec:
    def encode(self, strs: [str]) -> str:
        newStr = ""
        for string in strs:
            strNum = ""
            if len(string) == 0:
                strNum += "empty"
            else:
                for c in string:
                    if len(strNum) > 0:
                        strNum += ','
                    strNum += str(ord(c))
            if len(newStr) > 0:
                newStr += " "
            newStr += strNum
        return newStr
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> [str]:
        posAry = s.split()
        correct = []
        for p in posAry:
            if p == "empty":
                correct.append("")
                continue
            p_split = p.split(',')
            curstr = ""
            for c in p_split:
                curstr += chr(int(c))
            correct.append(curstr)
        return correct
        """Decodes a single string to a list of strings.
        """
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))