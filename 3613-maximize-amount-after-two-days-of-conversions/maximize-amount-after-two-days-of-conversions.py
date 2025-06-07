class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        def make_graph(pairs,rates):
            graph = defaultdict(list)
            for i in range(len(pairs)):
                s1 = pairs[i][0]
                s2 = pairs[i][1]
                graph[s1].append((s2,rates[i]))
                graph[s2].append((s1,(1/rates[i])))
            
            return graph
        
        def bfs(initial,graph,cost=1.0):

            queue = deque()
            queue.append((initial,cost))
            cost_dict = {}
            cost_dict[initial] = cost

            while queue:
                node, c = queue.popleft()

                if node in cost_dict and c < cost_dict[node]:
                    continue

                for neighbor, rate in graph[node]:
                    new_cost = c * rate
                    if neighbor not in cost_dict or new_cost > cost_dict[neighbor]:
                        queue.append((neighbor,new_cost))
                        cost_dict[neighbor] = new_cost

            return cost_dict


        graph1 = make_graph(pairs1, rates1)
        graph2 = make_graph(pairs2, rates2)

        first_graph_results = bfs(initialCurrency,graph1)
        max_result = float('-inf')

        for node,cost in first_graph_results.items():
            costdict = bfs(node,graph2,cost)
            max_result = max(max_result,costdict.get(initialCurrency,0.0))
        
        return max_result

        
        

                    
                
