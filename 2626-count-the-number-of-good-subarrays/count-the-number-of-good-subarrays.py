class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        right = left = 0
        windows = defaultdict(int)
        pair_count = defaultdict(int)
        ans = 0

        while left < len(nums) - 1:
            if right < len(nums):
                windows[nums[right]] += 1
                if windows[nums[right]] >= 2:
                    pair_count[nums[right]] += windows[nums[right]] - 1

            while sum([v for v in pair_count.values()]) >= k:
                ans += len(nums) - right if len(nums) - right else 1

                windows[nums[left]] -= 1
                if windows[nums[left]] >= 1:
                    pair_count[nums[left]] -= windows[nums[left]]
                left += 1
            
            if right < len(nums):
                right += 1
            else:
                left += 1

        return ans

                


        