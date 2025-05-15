class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        i = 0

        while i < len(s):
            j = 0
            while i < len(s) and j < numRows:
                rows[j].append(s[i])
                i += 1
                j += 1
            
            j = numRows - 2

            while  i < len(s) and j > 0:
                rows[j].append(s[i])
                j -= 1
                i += 1

        
        print(rows)

        return "".join(["".join(r) for r in rows])

        



            

