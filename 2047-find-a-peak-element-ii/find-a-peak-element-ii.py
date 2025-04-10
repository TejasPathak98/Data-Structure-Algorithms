class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2

            max_row_index = self.findIndex(mat,m,n,mid)

            max_number = mat[max_row_index][mid]
            left_number = mat[max_row_index][mid - 1] if mid  - 1 >= 0 else -1
            right_number = mat[max_row_index][mid + 1] if mid < n - 1 else -1

            if max_number > left_number and max_number > right_number:
                return [max_row_index,mid]
            elif max_number < left_number:
                right = mid - 1
            else:
                left = mid + 1

        
        return [-1,-1]
            

    def findIndex(self,mat,m,n,mid):
        index = -1
        val = -1

        for i in range(m):
            if mat[i][mid] > val:
                val = mat[i][mid]
                index = i

        return index