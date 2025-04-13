class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        
        def helper(col_idx):
            row_idx = -1
            row_val = -1

            for i in range(m):
                if mat[i][col_idx] > row_val:
                    row_val = mat[i][col_idx]
                    row_idx = i
            
            return row_idx

        l = 0
        h = n - 1

        while l <= h:
            mid = (l + h) // 2

            row_idx = helper(mid)


            left_number = mat[row_idx][mid - 1] if mid - 1 >= 0 else -1
            right_number = mat[row_idx][mid + 1] if mid + 1 < n else -1

            if  mat[row_idx][mid] > left_number and mat[row_idx][mid] > right_number:
                return [row_idx,mid]
            elif mat[row_idx][mid] < left_number:
                h = mid - 1
            else:
                l = mid + 1

        
        return [-1,-1]

