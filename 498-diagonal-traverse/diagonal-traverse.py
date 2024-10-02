class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        if m == 1 and n == 1:
            return [mat[0][0]]
        ans = []
        
        d = defaultdict(list)

        for i in range(m):
            for j in range(n):
                d[i + j].append(mat[i][j])
        
        for item in d.items():
            if item[0] % 2 == 0:
                [ans.append(x) for x in item[1][::-1]]
            else:
               [ans.append(x) for x in item[1]]
        
        return ans

        

        