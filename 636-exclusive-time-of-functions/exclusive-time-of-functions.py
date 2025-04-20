class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n

        stack = []

        for log in logs:
            job_id , operation , Time = log.split(":")
            job_id = int(job_id)
            Time = int(Time)

            if operation == "start":
                stack.append((job_id,Time))
            else:
                job_id , startTime = stack.pop()
                result[job_id] += (Time - startTime + 1)
                if stack:
                    result[stack[-1][0]] -= (Time - startTime + 1)
        
        return result