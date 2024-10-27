class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        ans = []
        my_dict = defaultdict(list)

        for i in range(n):
            for j in range(m):
                my_dict[i + j].append(mat[i][j])
        
        for k,val in my_dict.items():
            if k % 2 == 0:
                ans.extend(val[::-1])
            else:
                ans.extend(val)
        
        return ans
                
        