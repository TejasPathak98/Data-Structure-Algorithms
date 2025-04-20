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
        temp_sum = 0
        days = 1

        for weight in weights:
            if temp_sum + weight > ship_capacity:
                days += 1
                temp_sum = 0
            temp_sum += weight
        
        return days

