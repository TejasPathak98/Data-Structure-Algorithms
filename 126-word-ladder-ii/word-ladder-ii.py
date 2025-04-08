class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        depthMap = {}
        ans = []

        def dfs(word,seq):
            if word == beginWord:
                ans.append(seq[::-1][:])
                return
            
            steps = depthMap[word]

            for i in range(len(word)):
                original_ch = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + ch + word[i + 1:]

                    if word in depthMap and depthMap[word] + 1 == steps:
                        seq.append(word)
                        dfs(word,seq)
                        seq.pop()
                word = word[:i] + original_ch + word[i + 1:]
                    

        queue = deque([beginWord])
        depthMap[beginWord] = 1
        WordSet = set(wordList)
        WordSet.discard(beginWord)

        while queue:
            word = queue.popleft()
            steps = depthMap[word]

            if word == endWord:
                break
            
            for i in range(len(word)):
                original_ch = word[i]
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    word = word[:i] + ch + word[i + 1:]

                    if word in WordSet:
                        depthMap[word] = steps + 1
                        WordSet.discard(word)
                        queue.append(word)

                word = word[:i] + original_ch + word[i + 1:]

        wordList = set(wordList)

        if endWord in depthMap:
            seq = [endWord]
            dfs(endWord,seq)

        return ans
        