class Solution:
    def alienOrder(self, words: List[str]) -> str:
        charset = set("".join(words))
        graph, inDegree = self.helper(words,charset)

        if graph is None:
            return ""
        
        if not graph:
            return "".join(charset)

        return self.BFS(graph,inDegree,charset)
    
    def helper(self,words,charset):
        graph = defaultdict(list)
        inDegree = {char : 0 for char in charset}

        for word1,word2 in zip(words,words[1:]):

            if word1.startswith(word2) and len(word1) > len(word2):
                return None,None

            for c1,c2 in zip(word1,word2):
                if c1 != c2:
                    graph[c1].append(c2)
                    inDegree[c2] += 1
                    break
        
        return graph,inDegree
    
    def BFS(self,graph,inDegree,charset):
        

        queue = deque([char for char in charset if inDegree[char] == 0])
        result = ""

        while queue:
            ch = queue.popleft()
            result += ch

            for next_ch in graph[ch]:
                inDegree[next_ch] -= 1
                if inDegree[next_ch] == 0:
                    queue.append(next_ch)
        

        return result if len(result) == len(charset) else ""



        