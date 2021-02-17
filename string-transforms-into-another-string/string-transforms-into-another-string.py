class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        
        if str1 == str2:
            return True
        
        if len(set(str1)) == len(set(str2)) and len(set(str1)) == 26 and len(set(str2)) == 26:
            return False
        table = {}
        if len(str1) != len(str2):
            return False
        for s1,s2 in zip(str1,str2):
            if s1 in table:
                if table[s1] != s2:
                    return False
            else:
                table[s1] = s2
        return True
        