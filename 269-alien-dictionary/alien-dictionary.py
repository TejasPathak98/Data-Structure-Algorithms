class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        inDegree = {ch : 0 for word in words for ch in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLen = min(len(word1),len(word2))

            if word1[:minLen] == word2[:minLen] and len(word2) == minLen and len(word1) > minLen:
                return ""
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    inDegree[word2[j]] += 1
                    break
            
        queue = deque()

        for ch,key in inDegree.items():
            if key == 0:
                queue.append(ch)
        
        result = []

        while queue:

            node = queue.popleft()
            result.append(node)

            for nei in graph[node]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)

        
        print(result)

        return "".join(result) if len(result) == len(inDegree) else ""


