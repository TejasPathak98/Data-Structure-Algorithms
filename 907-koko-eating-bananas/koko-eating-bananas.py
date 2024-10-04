class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low,high = 1,max(piles)

        while low < high:

            mid = (low + high) // 2
            hours_taken = sum(math.ceil(pile / mid) for pile in piles)

            if hours_taken > h:
                low = mid + 1
            else:
                high = mid
        
        return low