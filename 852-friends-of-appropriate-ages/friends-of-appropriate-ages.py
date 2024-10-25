class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        amount_in_ages = [0] * 121
        prefix_sum_age = [0] * 121
        unique_age = set()

        for age in ages:
            amount_in_ages[age] += 1
            unique_age.add(age)
        
        for i in range(1,len(amount_in_ages)):
            prefix_sum_age[i] = prefix_sum_age[i - 1] + amount_in_ages[i]

        total = 0

        for age in unique_age:
            lb = age // 2 + 7
            hb = age
            
            requests = amount_in_ages[age] * (prefix_sum_age[hb] - prefix_sum_age[lb] - 1) 

            total += max(requests,0)
        
        return total
        