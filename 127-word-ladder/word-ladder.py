class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if len(endWord) > len(beginWord):
            return 0
        
        wordList = set(wordList)
        wordList.discard(beginWord)

        queue = deque([beginWord])
        count = 1

        visited = set()
        visited.add(beginWord)

        while queue:

            for _ in range(len(queue)):

                word = queue.popleft()

                if word == endWord:
                    return count
                
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in wordList and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
                
            count += 1
        

        return 0

        

