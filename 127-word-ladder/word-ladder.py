class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        queue = deque()
        queue.append(beginWord)

        if endWord not in wordSet:
            return 0
        
        distance = 1
        
        while queue:
            size = len(queue)

            for _ in range(size):

                word = queue.popleft()

                if word == endWord:
                    return distance

                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        
                        new_word = word[:i] + c + word[i + 1:]

                        if new_word in wordSet:
                            queue.append(new_word)
                            wordSet.remove(new_word)
            
            distance += 1
        
        return 0