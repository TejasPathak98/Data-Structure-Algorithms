class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(list)
        inDegree = {ch : 0 for word in words for ch in word}


        for word1,word2 in zip(words,words[1:]):
            l = min(len(word1),len(word2))

            if len(word1) > len(word2) and word1[:l] == word2:
                return ""

            for j in range(l):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    inDegree[word2[j]] += 1
                    print(word2[j],inDegree[word2[j]])
                    break
        
        print("br",inDegree)
        print(graph)

        result = []
        queue = deque()
        for ch, f in inDegree.items():
            if f == 0:
                queue.append(ch)

        print(queue)
        
        while queue:
            node = queue.popleft()

            result.append(node)

            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        print(result)
        
        if len(result) == len(inDegree):
            return "".join(result)
        else:
            return ""



