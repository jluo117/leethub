class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        def getContent(index,path):
            curContent = ""
            while path[index] != ')':
                curContent += path[index]
                index += 1
            return curContent
        table = {}
        for path in paths:
            subPath = path.split()[1:]
            folder_loc = path.split()[0]
            for file in subPath:
                index = 0
                fileName = ""
                while file[index] != '(':
                    fileName += file[index]
                    index += 1
                file_content = getContent(index+1,file)
                full_path = "{}/{}".format(folder_loc,fileName)
                if file_content in table:
                    table[file_content].append(full_path)
                else:
                    table[file_content] = [full_path]
        res = [ table[i]  for i in table  if len(table[i]) >= 2]
        return res