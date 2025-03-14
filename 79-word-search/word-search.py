class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.backtrack(i,j,board,word) == True:
                        return True
        
        return False


    # def backtrack(self,i,j,board,word):
    #     m = len(board)
    #     n = len(board[0])
    #     lw = len(word)
    #     visited = set()

    #     def helper(i,j,ptr,visited):
    #         if ptr == lw - 1:
    #             return True
            
    #         visited.add((i,j))
            
    #         for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
    #             x = i + dx
    #             y = j + dy

    #             if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[ptr + 1] or (x,y) in visited:
    #                 continue
                
    #             if helper(x,y,ptr + 1,visited):
    #                 return True


    #     return helper(i,j,0,visited)

    # This was failing becasue the visited set changes after the dfs calls, it passed by reference so it can happen that a dfs call goes and modifies the
    #the visited set and tracks but the visited remains changed, so the later dfs calls can lead to incorrect results
    #Hence we apply the bactracking principle to visited, we mark an element as visited then back track and then untrack it



    def backtrack(self,i,j,board,word):
        m = len(board)
        n = len(board[0])
        lw = len(word)

        def helper(i,j,ptr):
            if ptr == lw:
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[ptr]:
                return False #Incorrect, so we stop the operations further
            
            temp = board[i][j]
            board[i][j] = "#"  #marking as visited

            #recursing
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                if helper(i + dx,j + dy,ptr + 1) == True:
                    return True
 
            #unmarking
            board[i][j] = temp
            return False
        
        return helper(i,j,0)