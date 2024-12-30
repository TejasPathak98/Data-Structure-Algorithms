# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        n = reader.length()
        count = 1
        indx = -1

        for i in range(1,4):
            l = [j for j in range(1,5) if j != i]

            if reader.query(0,l[0],l[1],l[2]) != reader.query(1,2,3,4):
                indx = i 
            else:
                count += 1
        
        for i in range(4,n):
            if reader.query(0,1,2,3) != reader.query(1,2,3,i):
                indx = i 
            else:
                count += 1
        
        if count > n / 2:
            return 0
        elif count == n / 2:
            return -1
        else:
            return indx





