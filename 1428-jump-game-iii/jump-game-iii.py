class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # index_zero_pos = set()

        # for i in range(len(arr)):
        #     if arr[i] == 0:
        #         index_zero_pos.add(i)
        
        # def helper(pos):
        #     if pos in index_zero_pos:
        #         return True
            
        #     if pos + nums[pos] < len(nums):
        #         right_pos = pos + nums[pos]
        #     if pos - nums[pos] >= 0:
        #         left_pos = pos - nums[pos]

        #     helper(right_pos)
        #     helper(left_pos)

        # return helper(start)
        
        def helper(pos,visited):
            if pos < 0 or pos >= len(arr) or pos in visited:
                return False
            
            visited.add(pos)

            if arr[pos] == 0:
                return True
            
            if helper(pos + arr[pos],visited):
                return True
            #Short - circuiting and ending the function at the first sign of 'True'

            if helper(pos - arr[pos],visited):
                return True
            
            return False
        
        return helper(start,set())