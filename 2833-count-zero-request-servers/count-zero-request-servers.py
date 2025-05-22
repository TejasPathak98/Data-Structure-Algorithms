class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x : x[1])
        queries_with_idx = [(q,idx) for idx,q in enumerate(queries)]
        queries_with_idx.sort()

        left = 0
        right = 0
        ans = [0] * len(queries_with_idx)
        active_servers = defaultdict(int)
        total_servers = 0

        for q,idx in queries_with_idx:

            window_start = q - x
            

            while right < len(logs) and logs[right][1] <= q:

                if active_servers[logs[right][0]] == 0:
                    total_servers += 1
                
                active_servers[logs[right][0]] += 1

                right += 1

            
            while left < len(logs) and logs[left][1] < window_start:

                active_servers[logs[left][0]] -= 1

                if active_servers[logs[left][0]] == 0:
                    total_servers -= 1

                left += 1
            

            ans[idx] = n - total_servers
        
        return ans
                
                
