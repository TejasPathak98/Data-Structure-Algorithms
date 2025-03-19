class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #days = total_weight / Ship capacity

        l = max(weights)
        r = sum(weights)
        
        while l <= r:
            mid = (l + r) // 2

            no_of_days = self.helper(weights,mid)

            if no_of_days > days:
                l = mid + 1
            else:
                r = mid - 1

        
        return l
            
    def helper(self,weights,ship_weight):
        the_days = 0
        i = 0
        temp_sum = 0

        while i < len(weights):
            temp_sum += weights[i]
            if temp_sum == ship_weight:
                the_days += 1
                temp_sum = 0
                i += 1
            elif temp_sum > ship_weight:
                the_days += 1
                temp_sum = 0
            else:
                i += 1
        
        if temp_sum > 0:
            the_days += 1
        
        return the_days


            


