class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = tortoise = nums[0]

        while hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        tortoise = nums[0]
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]

        return tortoise


