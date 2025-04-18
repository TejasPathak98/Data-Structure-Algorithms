class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        city_dict = defaultdict(list)

        for src,dst in connections:
            city_dict[src].append((dst,True))
            city_dict[dst].append((src,False))
        
        queue = deque([0])
        capital_city = set()
        count = 0

        while queue:
            city = queue.popleft()
            capital_city.add(city)

            for nei , status in city_dict[city]:
                if nei not in capital_city:
                    queue.append(nei)

                    if status:
                        count += 1
            
        return count
