class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        # p1 = 0
        # p2 = len(nums) - 1
        # i = 0

        # while p1 < p2 and i <= p2:
        #     if nums[i] < pivot:
        #         temp = nums[p1]
        #         nums[p1] = nums[i]
        #         nums[i] = temp
        #         p1 += 1
        #     elif nums[i] > pivot:
        #         temp = nums[p2]
        #         nums[p2] = nums[i]
        #         nums[i] = temp
        #         p2 -= 1
        #         i -= 1
        #     i += 1

        # nums = nums[:p2 + 1] + list(reversed(nums[p2 + 1:]))

        # return nums

        #does not preserve order

        less = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
        

        return less + [pivot] * (len(nums) - len(less) - len(greater)) + greater



