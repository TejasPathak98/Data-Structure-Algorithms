class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #This is not a simple Topological Sort problem becasue its not a DAG
        #It is Euler Path Problem

        graph = defaultdict(list) 

        for src,dst in tickets:
            heapq.heappush(graph[src], dst) # the heap is used here for putting the lexicographically smallest elements first

        ans = []

        # def dfs(node):
        #     while graph[node]:
        #         next_node = heapq.heappop(graph[node])
        #         dfs(next_node)
        #     ans.append(node)
        
        # dfs("JFK")

        # return ans[::-1]

        #(ElogE)  ; O(E) + O(E) 

        stack = ["JFK"]

        while stack:
            while graph[stack[-1]]:
                stack.append(heapq.heappop(graph[stack[-1]]))
            ans.append(stack.pop())

        return ans[::-1]