class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def build_Trie():
            root = {}
            node = root
            for word in words:
                node = root
                for ch in word:
                    if ch not in node:
                        node = node.setdefault(ch,{})
                    else:
                        node = node[ch]
                node['#'] = word
            return root

        def dfs(x,y,trie):
            letter = board[x][y]
            node = trie[letter]
            word = node.pop('#',False)
            if word:
                result.append(word)

            temp = board[x][y]
            board[x][y] = "*"

            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] in node:
                    dfs(nx,ny,node)

            board[x][y] = temp
            if not node:
                trie.pop(letter)

        
        m = len(board)
        n = len(board[0])
        trie = build_Trie()
        result = []

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i,j,trie)

        return result








