class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        res = [0]*n
        ans = 0

        for r in roads:
            graph[r[0]].append(r[1])
            graph[r[1]].append(r[0])
        
        sorted_graph = sorted(graph.items(), key = lambda x : len(x[1]) ,reverse = True)

        val = n

        for x,_ in sorted_graph:
            res[x] = val
            val -= 1
        
        print(res)

        for i in range(len(roads)):
            ans += res[roads[i][0]] + res[roads[i][1]]

        return ans
        
        
        