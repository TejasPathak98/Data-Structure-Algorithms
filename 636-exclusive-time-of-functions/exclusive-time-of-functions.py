class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans = [0] * n
        stack = []
        for log in logs:
            id,behavior,time = log.split(":")
            id = int(id)
            time = int(time)

            if behavior == "start":
                stack.append(time)
            else:
                old_time = stack.pop()
                t = time - old_time + 1
                ans[id] += t

                for i in range(len(stack)):
                    stack[i] = stack[i] + t

        return ans



        