class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high) // 2
            x = sum(math.ceil(pile / mid) for pile in piles)
            if x > h:
                low = mid + 1
            else:
                high = mid - 1

        return low