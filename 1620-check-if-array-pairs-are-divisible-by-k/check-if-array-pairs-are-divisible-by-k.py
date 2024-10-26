class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mp = [0] * k

        for x in arr:
            rem = ((x%k) +k)%k
            mp[rem] += 1
        
        for i in range(k):
            if i == 0:
                if mp[i] % 2 != 0:
                    return False
            else:
                if mp[i] != mp[k - i]:
                    return False
        return True
        