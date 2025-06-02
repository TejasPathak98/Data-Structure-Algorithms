class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        diag = set()
        anti_diag = set()
        result = []

        def backtracking(level,temp):
            #print(level)

            if level == n:
                print("br")
                v = []
                for p in temp:
                    s = "." * p + "Q" + "." * (n - p - 1)
                    v.append(s)
                result.append(v)
                return
            
            for j in range(n):
                print(level)
                if j in col or (level + j) in diag or (level - j) in anti_diag:
                    continue
                
                col.add(j)
                diag.add(j + level)
                anti_diag.add(level - j)
                temp.append(j)

                #print(level + 1)
                backtracking(level + 1, temp)

                temp.pop()
                col.remove(j)
                diag.remove(j + level)
                anti_diag.remove(level - j)

        
        backtracking(0, [])

        return result




            