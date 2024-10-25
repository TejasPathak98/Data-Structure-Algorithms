class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ans = 0

        def helper(x,y):
            if y > x:
                return False
            if y > 100 and x < 100:
                return False
            if y <= 0.5 * x + 7:
                return False
            
            return True
            
        my_dict = defaultdict(int)
        for age in ages:
            my_dict[age] += 1
        
        for age1,count1 in my_dict.items():
            for age2,count2 in my_dict.items():
                if helper(age1,age2):
                    if age1 == age2:
                        ans += count1 * (count1 - 1)
                    else:
                        ans += count1 * count2
        
        return ans


        
        