class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ans = []
        # counter = Counter(nums)
        # counter = sorted(counter.items(),key = lambda x:x[1],reverse = True)
        # for number,frequency in counter:
        #     if k == 0:
        #         break
        #     ans.append(number)
        #     k -= 1
        
        # return ans
        #O(NLogN) ; O(N)


        counter = Counter(nums)
        return [number for number,_ in counter.most_common(k)]
        