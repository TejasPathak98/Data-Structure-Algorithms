class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]

        i = 0
        while i < len(s):
            
            j = 0
            while j < numRows and i < len(s):
                rows[j].append(s[i])
                i += 1
                j += 1

            j = numRows - 2

            while j > 0 and i < len(s):
                rows[j].append(s[i])
                j -= 1
                i += 1

        final_row = []
        for r in rows:
            final_row.extend(r)
        return "".join(final_row)


