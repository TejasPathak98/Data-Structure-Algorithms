class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        temp = 0
        ans = 0

        for num in nums:
            temp = temp + num
            if temp - k in dic:
                ans += dic[temp - k]
            dic[temp] += 1
        
        return ans

            
        