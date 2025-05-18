class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def valid_candy_group(group_size):
            groups = 0

            for candy in candies:
                groups += (candy // group_size)
            
            return groups >= k
        
        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if valid_candy_group(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans