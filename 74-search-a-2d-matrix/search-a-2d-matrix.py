class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if m == 1 and n == 1:
            if matrix[0][0] == target:
                return True
            else:return False
        
        l = 0
        r =  n*m - 1

        while l <= r:
            mid = (l + r) // 2
            row_idx = mid // n
            col_idx = mid % n



            if  matrix[row_idx][col_idx] == target:
                return True
            
            if matrix[row_idx][col_idx] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False