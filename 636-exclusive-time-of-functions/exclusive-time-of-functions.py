class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []

        for log in logs:
            id,func,time = log.split(":")
            id = int(id)
            time = int(time)

            if func == "start":
                stack.append((id,time))
            else:
                temp = time - stack.pop()[1] + 1
                ans[id] += temp

                if stack:
                    ans[stack[-1][0]] -= temp
        
        return ans
        