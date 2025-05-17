class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        #monotonic decreasing stack

        n = len(heights)
        stack = []
        ans = [0] * n

        i = 0

        while i < n:
            while stack and heights[i] > heights[stack[-1]]:
                ans[stack.pop()] += 1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
            i += 1

        return ans


