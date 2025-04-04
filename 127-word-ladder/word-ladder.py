class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def helper(w1,w2):
            l = len(w1)
            count = 0
            
            for j in range(l):
                if w1[j] == w2[j]:
                    count += 1
            if count == l - 1:
                return True
            else:
                return False

        queue = deque()

        queue.append(beginWord)
        steps = 1
        visited = set([beginWord])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node == endWord:
                    return steps
                
                for word in wordList:
                    if word not in visited and helper(word,node):
                        queue.append(word)
                        visited.add(word)
            
            steps += 1
        

        return 0

        #O(M×L×N) ; O(M +N)

        #Bidirectional BFS

        forward_queue = {beginWord}
        back_queue = {endWord}
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)
        count = 0
        wordList = set(wordList)

        while forward_queue and back_queue:

            if len(forward_queue) > len(back_queue):
                forward_queue , back_queue = back_queue , forward_queue

            count += 1
            next_level = set()

            for word in forward_queue:
                for i in len(word):
                    for ch in 'abcedfghijklmnopqrstuvwxyz':
                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in back_queue:
                            return count
                        
                        if new_word not in visited and new_word in wordList:
                            visited.add(new_word)
                            next_level.add(new_word)

            forward_queue = next_level

        return 0






