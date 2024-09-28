class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []

        for i in range(rows):
            for j in range(cols):
                res.append(matrix[i][j])
        
        def helper(arr,target):
            n = len(arr)

            i = 0
            j = n - 1

            while i <= j:
                mid = (i + j) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            
            return False
                


        return helper(res,target)


        