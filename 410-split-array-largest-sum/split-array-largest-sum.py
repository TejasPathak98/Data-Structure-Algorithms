class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_form_sum(Sum):
            curr_sum = 0
            count = 1

            for num in nums:

                if curr_sum  + num > Sum:
                    count += 1
                    curr_sum = num
                else:
                    curr_sum += num

            return count <= k

        low = max(nums)
        high = sum(nums)
        result = high

        while low <= high:
            mid = (low + high) // 2

            if can_form_sum(mid):
                result = mid
                high = mid -1 # try for smaller
            else:
                low = mid + 1 # try for larger


        
        return result


