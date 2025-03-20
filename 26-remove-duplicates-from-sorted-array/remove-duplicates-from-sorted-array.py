class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # n = len(nums)
        # num_set = set()
        # num_list = []

        # for num in nums:
        #     if num not in num_set:
        #         num_set.add(num)
        #         num_list.append(num)
                
        # nums.clear()
        # for x in num_list:
        #     nums.append(x)

        # return

        #Two-pointer approach

        i = 0

        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]


        return i + 1