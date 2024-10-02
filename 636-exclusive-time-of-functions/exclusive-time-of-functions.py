class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        if n == 0:
            return 0
        stack = deque()
        ans = [0] * n

        for log in logs:
            id,activity,timestamp = log.split(":")
            id = int(id)
            timestamp = int(timestamp)

            if activity == "start":
                stack.append((id,timestamp))
            else:
                id, start_time = stack.pop()
                ans[id] += timestamp - start_time + 1

                if stack:
                    ans[stack[-1][0]] -= timestamp - start_time + 1
        
        return ans