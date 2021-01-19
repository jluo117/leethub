class Solution:
    def simplifyPath(self, path: str) -> str:
        splitOrder = path.split("/")
        stk = []
        for folder in splitOrder:
            if folder == "." or folder == "":
                continue
            if folder == "..":
                if len(stk) > 0:
                    stk.pop()
                continue
            stk.append(folder)
        curStr = ""
        for val in stk:
            curStr += "/"+val
        if len(curStr) == 0:
            curStr += '/'
        return curStr
