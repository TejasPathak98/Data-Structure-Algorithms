class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        dic = defaultdict(int)

        for i in range(len(nums)):
            dic[nums[i]] += 1
        
        dic = dict(sorted(dic.items(), key = lambda x : x[1],reverse=True))

        ans = []
        var = 0

        for key,val in dic.items():
            var += 1
            if var > k:
                break
            else:
                ans.append(key)
        
        return ans





        