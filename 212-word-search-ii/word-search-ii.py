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


        def dfs(i,j,Trie):
            letter = board[i][j]
            curr = Trie[letter]

            word = curr.pop('#',False)

            if word:
                result.append(word)

            
            temp = board[i][j]

            board[i][j] = "*"

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in curr:
                    dfs(ni,nj,curr)

            board[i][j] = temp

            
            if not curr:
                Trie.pop(letter)

        Trie = build_trie(words)
        result = []

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] in Trie:
                    dfs(i,j,Trie)

        
        return result


                    


