class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):

                if board[r][c] == ".":
                    continue 
                
                val = board[r][c]

                if val in rows[r]:
                    return False
                else:
                    rows[r].add(val)
                
                if val in cols[c]:
                    return False
                else:
                    cols[c].add(val)
                
                idx = (r // 3)*3 + c // 3
                if val in boxes[idx]:
                    return False
                else:
                    boxes[idx].add(val)
        
        return True
        