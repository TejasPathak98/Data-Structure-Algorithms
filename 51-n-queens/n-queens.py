class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
    #     if n == 1:
    #         return [["Q"]]

    #     result = []
    #     board = [["."] * n for _ in range(n)]
    #     col_set = []
    #     row_set = []


    #     def diag_helper(col1,row1,col2,row2):
    #         if ((col1 - col2) / (row1 - row2)) in [-1,1]:
    #             return True
    #         return False

    #     def backtrack(col,row_num,total_placed,row_set,col_set):
    #         if total_placed == n:
    #             temp = []
    #             for r in board:
    #                 temp.append("".join(r[:]))
    #             result.append(temp)
    #             return

    #         flag = False

    #         for i in range(n):
    #             if i in col_set:
    #                 continue
    #             for k in range(len(col_set)):
    #                 if diag_helper(col_set[k],row_set[k],i,row_num + 1) == True:
    #                     flag = True
    #                     break
                
    #             if flag:
    #                 flag = False
    #                 continue

    #             col_set.append(i)
    #             row_set.append(row_num + 1)
    #             board[row_num + 1][i] = "Q"
    #             backtrack(i, row_num + 1, total_placed + 1,row_set,col_set)
    #             board[row_num + 1][i] = "."
    #             col_set.pop()
    #             row_set.pop()


    #     for i in range(n):
    #         board[0][i] = "Q"
    #         row_set.append(0)
    #         col_set.append(i)
    #         backtrack(i,0,1,row_set,col_set)
    #         board[0][i] = "."
    #         col_set.pop()
    #         row_set.pop()

    #     return result

    # # O(N * N!)  ; O(N! * N ^2) ...due to diagonal checks and board space respectively


        result = []
        col = set()
        diag = set()
        anti_diag = set()
        queens = [-1] * n

        def backtrack(row):
            if row == n:
                board = []
                for r in queens:
                    res_str = r * "." + "Q" + "." * (n - r - 1)
                    board.append(res_str)
                result.append(board)
                return
        

            for c in range(n):
                if c in col or (row + c) in diag or (row - c) in anti_diag:
                    continue
                
                queens[row] = c
                col.add(c)
                diag.add(c + row)
                anti_diag.add(row - c)

                backtrack(row + 1)

                col.remove(c)
                diag.remove(c + row)
                anti_diag.remove(row - c)

        
        backtrack(0)
        return result
                
