class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        result = [-1] * len(queries)

        if x not in nums:
            return result
        
        x_dict = defaultdict()

        occ_counter = 0
        for i, num in enumerate(nums):
            if num == x:
                occ_counter += 1
                x_dict[occ_counter] = i
        
        for j,query in enumerate(queries):
            if query in x_dict:
                result[j] = x_dict[query]

        
        return result