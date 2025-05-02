class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #state will be node + stops until then instead of just no_type_check_decorator

        # in basic Dijskstra we can prune at push
        #here it is safer to prune after pop as we do not have best_Cost kind of dict upfront which we can maintain for the combined state...it will be difficult as it will become a 
        #2 dimensional array 
        #in BFS, once we enqueue we know for sure that its the least cost...part of level order traversal
        #that is not the case with dijkstra, here the cost is guaranteed to be minimum once we pop it out

        heap = []
        best_dict = {}
        heappush(heap, (0,src,0))

        graph = defaultdict(list)

        for u,v,w in flights:
            graph[u].append((v,w))

        while heap:

            cost,node,stops = heappop(heap)

            if stops > k + 1:
                continue

            if node == dst:
                return cost

            if (node,stops) in best_dict and best_dict[(node,stops)] <= cost:
                continue
            
            best_dict[(node,stops)] = cost


            for nei,w in graph[node]:
                new_cost = w + cost
                if stops <= k:
                    heappush(heap, (new_cost,nei,stops + 1))

        
        return -1