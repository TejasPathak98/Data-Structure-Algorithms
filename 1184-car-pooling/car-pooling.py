class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = len(trips)
        left = 1e9 
        right = 0
        prefix = [0] * 1001
        cap = 0

        for tpl in trips:
            prefix[tpl[1]] += tpl[0]
            prefix[tpl[2]] -= tpl[0] 
            left = min(left,tpl[1])
            right = max(right,tpl[2])

        for i in range(left,right + 1):
            cap += prefix[i]
            if cap > capacity:
                return False 
        
        return True


            

        