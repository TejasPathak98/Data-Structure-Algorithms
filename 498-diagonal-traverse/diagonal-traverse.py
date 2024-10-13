class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        ans = []
        dic = defaultdict(list)

        for i in range(n):
            for j in range(m):
                dic[i + j].append(mat[i][j])
        
        for k,val in dic.items():
            if k % 2 == 0:
                val = val[::-1]
                ans.extend(val)
            else:
                ans.extend(val)
            
        return ans

        