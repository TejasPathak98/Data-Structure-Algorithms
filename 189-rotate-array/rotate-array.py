class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:return
        k = k % len(nums)

        my_dict = defaultdict(int)
        for i in range(len(nums)):
            my_dict[i] = nums[i]

        for i in range(len(nums)):
            new_pos = (i + k) % len(nums)
            nums[new_pos] = my_dict[i]
        
