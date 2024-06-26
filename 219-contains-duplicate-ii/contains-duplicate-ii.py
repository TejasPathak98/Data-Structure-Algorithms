class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                dic.get(nums[i]).append(i) 
            else:
                dic[nums[i]] = [i] 
        
        for l in dic.values():
            for i in range(1,len(l)):
                if abs(l[i] - l[i - 1]) <= k:
                    return True  
        
        return False

        