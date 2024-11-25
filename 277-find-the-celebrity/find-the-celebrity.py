# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        possibleCelebSet = set()

        for i in range(n):
            possibleCelebSet.add(i)
        
        while len(possibleCelebSet) > 1:
            a,b = possibleCelebSet.pop() , possibleCelebSet.pop()
            if knows(a,b):
                possibleCelebSet.add(b)
            else:
                possibleCelebSet.add(a)
        
        celeb = possibleCelebSet.pop()
        for i in range(n):
            if i == celeb:
                continue
            
            if knows(i,celeb) == False:
                return -1
            
            if knows(celeb,i) == True:
                return -1
        return celeb
        