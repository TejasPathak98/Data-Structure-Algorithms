class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_str = ""
        for row in board:
            board_str += "".join(row)
        
        print(board_str)

        board_counter = Counter(board_str)
        word_counter = Counter(word)

        for ch in word:
            if word_counter[ch] > board_counter[ch]:
                print("Here")
                return False
        
        m = len(board)
        n = len(board[0])

        def backtracking(i,j,pos):
            if pos == len(word):
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or word[pos] != board[i][j]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = i + dx
                y_ = j + dy

                if backtracking(x_, y_, pos + 1):
                    return True


            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtracking(i,j,0):
                        return True
        
        return False



        
