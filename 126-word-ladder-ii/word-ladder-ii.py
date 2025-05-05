class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        ans = []
        depthMap = {}

        def dfs(seq,word):
            print(seq)
            if word == beginWord:
                ans.append(seq[::-1][:])
                return
            
            steps = depthMap[word]

            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in depthMap and depthMap[new_word] + 1 == steps:
                        seq.append(new_word)
                        dfs(seq,new_word)
                        seq.pop()

        wordList = set(wordList)
        depthMap[beginWord] = 1
        #wordList.discard(beginWord)
        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        while queue:

            word = queue.popleft()

            steps = depthMap[word]

            if word == endWord:
                break
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in wordList and new_word not in visited:
                        queue.append(new_word)
                        depthMap[new_word] = steps + 1
                        visited.add(new_word)

        
        
        if endWord in depthMap:
            dfs([endWord],endWord)
        
        return ans
                    




