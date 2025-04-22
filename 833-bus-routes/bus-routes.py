class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        bus_stop_to_route_mapping = defaultdict(list)
        stop_visited = set()
        routes_visited = set()
        queue = deque()

        for bus_idx,route in enumerate(routes):
            for busStop in route:
                bus_stop_to_route_mapping[busStop].append(bus_idx)
        
        queue.append(source)
        stop_visited.add(source)

        stops = 0

        while queue:

            for _ in range(len(queue)):

                stop = queue.popleft()

                if stop == target:
                    return stops

                for bus_idx in bus_stop_to_route_mapping[stop]:
                    if bus_idx not in routes_visited:
                        routes_visited.add(bus_idx)
                        for new_stop in routes[bus_idx]:
                            if new_stop not in stop_visited:
                                stop_visited.add(new_stop)
                                queue.append(new_stop)

            stops += 1
        

        return -1
                                
                


