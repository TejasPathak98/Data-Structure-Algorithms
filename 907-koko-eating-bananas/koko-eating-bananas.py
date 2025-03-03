class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #time = Bananas / k

        l = 1
        r = max(piles)

        while l <= r:
            mid = (l + r) // 2
            
            time = sum(math.ceil(pile/mid) for pile in piles)

            if time > h:
                l = mid + 1
            else:
                r = mid - 1
        

        return l

