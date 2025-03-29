class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stops_to_bus_map = defaultdict(list)

        for bus,route in enumerate(routes):
            for stop in route:
                stops_to_bus_map[stop].append(bus)
        
        queue = deque()
        queue.append((source,0))
        visited_stop = set([source])
        visited_bus = set()


        while queue:
            stop, buses_taken = queue.popleft()

            if stop == target:
                return buses_taken
            
            for new_bus in stops_to_bus_map[stop]:
                if new_bus not in visited_bus:
                    for new_stop in routes[new_bus]:
                        if new_stop == target:
                            return buses_taken + 1
                        if new_stop not in visited_stop:
                            visited_stop.add(new_stop)
                            visited_bus.add(new_bus)
                            queue.append((new_stop,buses_taken + 1))

        
        return -1

