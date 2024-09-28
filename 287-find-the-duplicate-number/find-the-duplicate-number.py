class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]

        while tortoise:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        tortoise = nums[0]
        while tortoise != hare:
            hare = nums[hare]
            tortoise = nums[tortoise]
        
        return tortoise
         
        