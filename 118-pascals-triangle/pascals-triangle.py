class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[]] 
        
        elif numRows == 1:
            return [[1]] 
        
        prevRow = self.generate(numRows - 1) 
        newRow = [1] * numRows

        for i in range(1, numRows - 1):
            newRow[i] = prevRow[-1][i-1] + prevRow[-1][i] 
        
        prevRow.append(newRow)
        return prevRow




        