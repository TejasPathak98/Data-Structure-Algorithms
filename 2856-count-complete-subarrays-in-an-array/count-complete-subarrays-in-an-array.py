class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = Counter(nums)
        distinct_elements = len(counter)

        l = 0
        r = 0

        count = 0
        num_dict = defaultdict(int)

        while r < len(nums):
            num_dict[nums[r]] += 1

            while len(num_dict) == distinct_elements:
                count += len(nums) - r
                num_dict[nums[l]] -= 1
                if num_dict[nums[l]] == 0:
                    del num_dict[nums[l]]
                l += 1

            r += 1

        return count




