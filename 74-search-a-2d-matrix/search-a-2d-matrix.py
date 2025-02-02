class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l = 0
        r = m*n - 1

        while l <= r:
            mid = (l + r) // 2

            r_pos = mid // n
            c_pos = mid  % n

            if matrix[r_pos][c_pos] == target:
                return True
            
            elif matrix[r_pos][c_pos] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        