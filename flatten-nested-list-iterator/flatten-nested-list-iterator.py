# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.curIndex = 0
        def helper(curList):
            res = []
            for n in curList:
                if n.isInteger():
                    res.append(n.getInteger())
                else:
                    res += helper(n.getList())
            return res
        self.res = helper(nestedList)
        
    
    def next(self) -> int:
        pull = self.res[self.curIndex]
        self.curIndex += 1
        return pull
            
    
    def hasNext(self) -> bool:
        return self.curIndex < len(self.res)
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())