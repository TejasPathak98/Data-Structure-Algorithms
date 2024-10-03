class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[]for _ in range(numRows)]
        d = 1
        idx = 0

        for ch in s:
            rows[idx].append(ch)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d
        
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        
        return ''.join(rows)
        

        

        