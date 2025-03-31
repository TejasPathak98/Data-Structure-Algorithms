class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(i,j,trie):
            letter = board[i][j]
            curr = trie[letter]

            w = curr.pop('#',False)

            if w:
                result.append(w)
            
            board[i][j] = "*"

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                x = dx + i
                y = dy + j

                if 0 <= x < m and 0 <= y < n and board[x][y] in curr:
                    dfs(x,y,curr)

            board[i][j] = letter

            if not curr:
                trie.pop(letter)

        trie = {}
        result = []
        m = len(board)
        n = len(board[0])

        for word in words:
            curr = trie
            for letter in word:
                curr = curr.setdefault(letter,{})
            curr['#'] = word
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i,j,trie)
        
        return result