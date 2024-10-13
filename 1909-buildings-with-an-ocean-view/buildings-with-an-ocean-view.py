class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        ans.append(len(heights) - 1)
        max_size = heights[len(heights) - 1]

        for i in range(len(heights) - 2, - 1, -1):
            if heights[i] > max_size:
                ans.append(i)
                max_size = heights[i]

        return ans[::-1]


        