class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        n = len(heights) - 1
        ans.append(n)
        i = n - 1
        max_height = heights[n]
        print(max_height)

        while i >= 0:
            if heights[i] > max_height:
                ans.append(i)
                max_height = heights[i]
            i -= 1
            
        ans = sorted(ans)
        return ans
        