class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        left = nums[:mid]
        right = nums[mid:]

        left = self.sortArray(left)
        right = self.sortArray(right)

        return self.merge(left,right)

    def merge(self,left,right):
        i = j = 0
        result = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result