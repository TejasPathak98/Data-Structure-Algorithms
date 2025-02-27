class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] 
        cols = [set() for _ in range(9)] 
        boxes =  [set() for _ in range(9)] 

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                number = int(board[i][j])

                if number in rows[i]:
                    return False
                else:
                    rows[i].add(number)

                if number in cols[j]:
                    
                    return False
                else:
                    cols[j].add(number)
                
                box_idx = (i // 3)*3 + (j // 3)

                if number in boxes[box_idx]:
                    
                    return False
                else:
                    boxes[box_idx].add(number)
        
        return True
        