class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        count = 0
        wordList = set(wordList)

        while queue:
            size = len(queue)
            count += 1
            
            for _ in range(size):
                word = queue.popleft()
                if word == endWord:
                    return count
            
                for i, ch in enumerate(word):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word not in visited and new_word in wordList:
                            queue.append(new_word)
                            visited.add(new_word)
        
        return 0
