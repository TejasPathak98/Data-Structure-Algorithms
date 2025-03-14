class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        lw = len(word)

        board_freq = Counter(sum(board,[]))
        word_freq = Counter(word)

        for char in word:
            if word_freq[char] > board_freq.get(char,0):
                return False
        
        def neighbor_rarity(x,y):
            counter = 0
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                if x + dx >= 0 and x + dx  < m and y +dy >= 0 and y + dy < n and board_freq.get(board[x + dx][y + dy],0) > 0:
                    counter += board_freq.get(board[x + dx][y + dy])
            return counter
        
        positions = []

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    positions.append((i,j))

        positions.sort(key = lambda pos : neighbor_rarity(*pos))

        def backtrack(x,y,ptr):
            if ptr == lw:
                return True
            
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[ptr]:
                return False
            
            temp = board[x][y]
            board[x][y] = "#"

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                if backtrack(x + dx,y + dy,ptr + 1):
                    return True
                
            board[x][y] = temp
            return False

        
        for i,j in positions:
            if backtrack(i,j,0):
                return True
        
        return False


