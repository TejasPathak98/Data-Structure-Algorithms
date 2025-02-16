class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src,dst in sorted(tickets):
            graph[src].append(dst)
        
        itinerary = []

        def dfs(node):

            while graph[node]:
                new_node = graph[node].pop(0)
                dfs(new_node)
            itinerary.append(node)
        
        dfs("JFK")

        return itinerary[::-1]
