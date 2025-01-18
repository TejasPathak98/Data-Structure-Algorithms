class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        c = sorted(c.items(),key = lambda x : x[1], reverse= True)

        ans = []


        for key,v in c:
            ans.append(key)
        
        return ans[:k]

        