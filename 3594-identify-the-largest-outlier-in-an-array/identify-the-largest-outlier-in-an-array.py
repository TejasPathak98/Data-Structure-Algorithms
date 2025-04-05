class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        final_outlier = float("-inf")
        
        num_dict = defaultdict(int)

        for num in nums:
            num_dict[num] += 1
        
        for num in num_dict:

            potential_outlier = total_sum - 2 * num
            #this is because : total_sum = sum of special elements + outlier + (other element, which is the sum of special elements)

            if potential_outlier in num_dict:
                if potential_outlier != num or num_dict[potential_outlier] > 1:
                    final_outlier = max(final_outlier,potential_outlier)


        
        return final_outlier

        