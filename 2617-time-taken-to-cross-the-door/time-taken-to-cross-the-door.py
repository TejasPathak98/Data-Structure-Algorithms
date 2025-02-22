class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        entry_pool = deque()
        exit_pool = deque()
        i = 0
        ans = [[0] for _ in range(len(arrival))]
        curr_time = 0
        prev_state = 1

        while i <len(arrival) or entry_pool or exit_pool:
            while i < len(arrival) and arrival[i] <= curr_time:
                if state[i] == 0:
                    entry_pool.append(i)
                else:
                    exit_pool.append(i)
                i += 1
            if prev_state == 1:
                if exit_pool:
                    ans[exit_pool.popleft()] = curr_time
                elif entry_pool:
                    ans[entry_pool.popleft()] = curr_time
                    prev_state = 0
            else:
                if entry_pool:
                    ans[entry_pool.popleft()] = curr_time
                elif exit_pool:
                    ans[exit_pool.popleft()] = curr_time
                    prev_state = 1
                else:
                    prev_state = 1
            curr_time += 1
        
        return ans
                


