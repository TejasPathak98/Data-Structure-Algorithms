class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord not in wordList:
        #     return 0

        # queue = deque([beginWord])
        # visited = set()
        # visited.add(beginWord)
        # count = 0
        # wordList = set(wordList)

        # while queue:
        #     size = len(queue)
        #     count += 1
            
        #     for _ in range(size):
        #         word = queue.popleft()
        #         if word == endWord:
        #             return count
            
        #         for i, ch in enumerate(word):
        #             for c in "abcdefghijklmnopqrstuvwxyz":
        #                 new_word = word[:i] + c + word[i + 1:]
        #                 if new_word not in visited and new_word in wordList:
        #                     queue.append(new_word)
        #                     visited.add(new_word)
        
        # return 0

        # #O(V + E) ; O(V)  

        if endWord not in wordList:
            return 0

        forward_queue = {beginWord}
        back_queue = {endWord}
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)
        wordList = set(wordList)
        count = 1


        while forward_queue and back_queue:
            if len(forward_queue) > len(back_queue):
                forward_queue , back_queue = back_queue , forward_queue

            count += 1
            next_level = set()

            for word in forward_queue:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new_word = word[:i] + ch + word[i + 1:]

                        if new_word in back_queue: # Intersection of the 2 queue's
                            return count

                        if new_word not in visited and new_word in wordList:
                            visited.add(new_word)
                            next_level.add(new_word)


            forward_queue = next_level

        return 0 