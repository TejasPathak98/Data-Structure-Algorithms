class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordList = set(wordList)
        wordList.discard(beginWord)
        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        steps = 1 


        while queue:
            for _ in range(len(queue)):

                word = queue.popleft()

                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + ch + word[i + 1:]
                        if new_word in wordList and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
            
            steps += 1

        
        return 0



