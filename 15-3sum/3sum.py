class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()

        # result = []

        # for i in range(len(nums) - 2):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     j = i + 1
        #     k = len(nums) - 1

        #     while j < k:

        #         Sum = nums[i] + nums[j] + nums[k]

        #         if Sum == 0:
        #             result.append([nums[i],nums[j],nums[k]])

        #             while j < k and nums[j] == nums[j + 1]:
        #                 j += 1

        #             while j < k and nums[k] == nums[k - 1]:
        #                 k -= 1

        #             j += 1
        #             k -= 1

        #         elif Sum > 0:
        #             k -= 1
        #         else:
        #             j += 1

    
        #return result

        #O(N^2) ; O(1)

        nums.sort()
        ans = set()

        for i,v in enumerate(nums):
            if i >= 1 and nums[i - 1] == v:
                continue
            triplet_dict = defaultdict(int)

            for x in nums[i + 1:]:
                if x not in triplet_dict:
                    triplet_dict[(-x-v)] = 1
                else:
                    ans.add((x,v,-x-v))

        return list(ans)




    
        





                

