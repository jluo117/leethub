class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        def shouldRemove(prev,cur):
            if prev == cur:
                return False
            if prev.lower() == cur.lower():
                return True
            return False
        for c in s:
            if len(stk) > 0 and shouldRemove(stk[-1],c):
                stk.pop()
                continue
            stk.append(c)
        newStr = ""
        for c in stk:
            newStr += c
        return newStr
        
