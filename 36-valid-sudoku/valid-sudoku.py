class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                digit = board[i][j]

                if digit == ".":
                    continue

                if digit in rows[i]:
                    return False
                else:
                    rows[i].add(digit)
                
                if digit in cols[j]:
                    return False
                else:
                    cols[j].add(digit)
                
                box_idx = (i // 3) * 3 + (j // 3)

                if digit in boxes[box_idx]:
                    return False
                else:
                    boxes[box_idx].add(digit)

        return True