class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_trie(words):
            root = {}
            
            for word in words:
                curr = root
                for ch in word:
                    if ch not in curr:
                        curr[ch] = {}
                    curr = curr[ch]
                curr['#'] = word

            return root

        
        def dfs(x,y,trie):
            letter = board[x][y]
            curr = trie[letter]

            w = curr.pop('#',False)

            if w:
                result.append(w)
            
            temp = board[x][y]

            board[x][y] = "*"

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_ = x + dx
                y_ = y + dy

                if 0 <= x_ < m and 0 <= y_ < n and board[x_][y_] in curr:
                    dfs(x_,y_,curr)

            board[x][y] = temp
            
            if not curr:
                trie.pop(letter)

        result = []
        trie = build_trie(words)
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie: 
                    dfs(i,j,trie)


        return result