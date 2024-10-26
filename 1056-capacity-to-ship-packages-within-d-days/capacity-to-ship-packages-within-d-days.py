class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            m = (l + r) // 2
            if self.helper(m,weights) > days:
                l = m + 1
            else:
                r = m
    
        return l

    def helper(self,ship_capacity,weights):
        days = 1
        capacity = 0

        for weight in weights:
            if capacity + weight > ship_capacity:
                days += 1
                capacity = weight
            else:
                capacity += weight
        
        return days
    
        




        