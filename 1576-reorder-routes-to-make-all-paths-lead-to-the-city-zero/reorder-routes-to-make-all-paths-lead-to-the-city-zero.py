class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        city_dict = defaultdict(list)

        for src,dst in connections:
            city_dict[src].append((dst,True))
            city_dict[dst].append((src,False))
        
        queue = deque([0])
        visited = set()
        visited.add(0)
        count = 0

        while queue:
            city = queue.popleft()

            for nei , direction in city_dict[city]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

                    if direction:
                        count += 1

        
        return count

