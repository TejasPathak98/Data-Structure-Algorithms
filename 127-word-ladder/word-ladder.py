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
        

        
        graph = []

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




