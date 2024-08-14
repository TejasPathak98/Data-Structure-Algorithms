class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque(rooms[0])

        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
            visited.add(room)
            if len(visited) == len(rooms):
                return True

        if len(visited) == len(rooms):
                return True
        else:
            return False     