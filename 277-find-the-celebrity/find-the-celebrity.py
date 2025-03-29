# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0 # intially assume that the first candidate is the celebrity

        for i in range(n):
            if candidate != i:
                if knows(candidate,i):
                    candidate = i #if candidate knows i, its not celebrity ; if it does not know i then i cannot be celebrity
        
        for i in range(n): # this check is to see if candidate is known by everyone and knows none
            if candidate != i:
                if knows(candidate,i) or not knows(i,candidate):
                    return -1
        
        return candidate
        