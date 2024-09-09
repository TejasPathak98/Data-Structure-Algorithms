class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        hmap = defaultdict(int)
        n = len(nums)

        for i in range(n):
            hmap[nums[i]] += 1
        
        for i in range(1,n + 1):
            if i not in hmap:
                ans.append(i)

        return ans
        