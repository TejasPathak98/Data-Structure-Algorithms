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
        self.nestedList = nestedList
        self.finalList = []
        n = len(self.nestedList)
        self.ptr = 0
        for i in range(n):
            if nestedList[i].isInteger():
                self.finalList.append(nestedList[i].getInteger())
            else:
                self.finalList.extend(self.helper(nestedList[i].getList()))

    def helper(self,nested):
        finalList = []
        for i in range(len(nested)):
            if nested[i].isInteger():
                finalList.append(nested[i].getInteger())
            else:
                finalList.extend(self.helper(nested[i].getList()))
        return finalList

        
    def next(self) -> int:
        x = self.finalList[self.ptr]
        self.ptr += 1
        return x

    def hasNext(self) -> bool:
        return self.ptr < len(self.finalList)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())