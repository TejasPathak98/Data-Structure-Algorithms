class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # days = total / w

        l = max(weights)
        r = sum(weights)

        while l < r:

            mid = (l + r) // 2

            time = self.helper(mid,weights)

            if time <= days:
                r = mid
            else:
                l = mid + 1

        return l
        
    def helper(self,ship_capacity,weights):
        days = 0
        curr = 0

        for idx,weight in enumerate(weights):
            curr += weight

            if curr == ship_capacity:
                days += 1
                curr = 0
            elif curr > ship_capacity:
                days += 1
                curr = weight
        
        if curr:
            days += 1
        


        return days

