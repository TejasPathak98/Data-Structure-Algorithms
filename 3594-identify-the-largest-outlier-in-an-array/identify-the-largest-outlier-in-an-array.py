class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        max_outlier = float("-inf")
        total_sum = sum(nums)

        counter = Counter(nums)

        #formula : total_sum = 2*num + outlier

        for num in nums:
            potential_outlier = total_sum - 2*num

            if potential_outlier in counter:
                if potential_outlier != num or counter[potential_outlier] > 1:
                    max_outlier = max(max_outlier,potential_outlier)
        

        return max_outlier