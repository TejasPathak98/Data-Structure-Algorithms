class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        bus_stop_to_bus_mapping = defaultdict(list)

        for bus_idx,route in enumerate(routes):
            for stop in route:
                bus_stop_to_bus_mapping[stop].append(bus_idx)
        
        queue = deque([(source)])
        visited_stops = set([(source)])
        visited_buses = set()
        buses_taken = 0

        while queue:
            for _ in range(len(queue)): #Expanding the whole queue(bus routes here)

                stop = queue.popleft()
                if stop == target:
                    return buses_taken
                
                for bus in bus_stop_to_bus_mapping[stop]:
                    if bus not in visited_buses:
                        visited_buses.add(bus)
                        for new_stop in routes[bus]:
                            if new_stop not in visited_stops:
                                queue.append(new_stop)
                                visited_stops.add(new_stop)
            
            buses_taken += 1


        
        return -1
