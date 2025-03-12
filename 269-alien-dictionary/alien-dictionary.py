class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        inDegree = {char : 0 for word in words for char in word}
        result = []

        # Buidling the graph and inDegree Map
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_word_len = min(len(word1),len(word2))

            if word1[:min_word_len] == word2[:min_word_len] and len(word1) > len(word2):
                return ""
            
            for j in range(min_word_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        inDegree[word2[j]] += 1
                    break
        
        queue = deque([char for char in inDegree if inDegree[char] == 0])

        while queue:
            c = queue.popleft()
            result.append(c)

            for neighbor in graph[c]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)


        return "".join(result) if len(inDegree) == len(result) else ""