class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        initial_state = "0000"
        deadends = set(deadends)
        visited = set() #We only need to store states and not counts....If I reach the state with different count, do I need it ? NO....because the first will be the shortest count

        if initial_state in deadends:
            return -1

        queue =deque([(initial_state,0)])
        visited.add(initial_state)

        while queue:
            node , count= queue.popleft()

            if node == target:
                return count

            for i in range(4):
                digit = int(node[i])
                for move in [-1,1]:
                    new_digit = (digit + move) % 10 #works becase -1 % 10 = 9 ; -2 % 10 = 8 in Python(wrap around)

                    new_node = node[:i] + str(new_digit) + node[i + 1:]

                    if new_node not in visited and new_node not in deadends:
                        queue.append((new_node,count + 1))
                        visited.add(new_node)

        return -1


