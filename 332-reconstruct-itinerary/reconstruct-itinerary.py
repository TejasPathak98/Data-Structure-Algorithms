class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Euler Path Problem
        #The nodes have to be traversed in a post order fashion, explore all the paths and then add the current node ; there is reversing at the end

        graph = defaultdict(list)

        for u,v in tickets:
            heapq.heappush(graph[u], v)

        ans = []

        def dfs(node):
            while graph[node]:
                neighbor = heapq.heappop(graph[node])
                dfs(neighbor)
            ans.append(node)

        dfs("JFK")
        return ans[::-1]
