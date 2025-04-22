class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie(words):
            Trie = {}

            for word in words:
                curr = Trie
                for ch in word:
                    if ch not in curr:
                        curr[ch] = {}
                    curr = curr[ch]
                curr['#'] = word
        
            return Trie

        
        def dfs(x,y,Trie):
            letter = board[x][y]
            curr = Trie[letter]

            word = curr.pop('#',False)
            if word:
                result.append(word)
            
            temp = board[x][y]

            board[x][y] = "*"

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in curr:
                    dfs(nx,ny,curr)

            
            board[x][y] = temp

            if not curr:
                Trie.pop(letter)

        m = len(board)
        n = len(board[0])
        Trie = build_trie(words)
        result = []

        for i in range(m):
            for j in range(n):
                if board[i][j] in Trie:
                    dfs(i,j,Trie)
        

        return result

