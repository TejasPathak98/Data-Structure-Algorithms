class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def getNext(x):
            return (x + nums[x]) % len(nums)
        
        for i in range(len(nums)):
            slow = i
            fast = getNext(i)
            while True:
                if slow == getNext(slow) or fast == getNext(fast):
                    break
                if nums[slow] * nums[getNext(slow)] < 0  or nums[fast] * nums[getNext(fast)] < 0:
                    break
                slow = getNext(slow)
                fast = getNext(getNext(fast))
                if slow == fast:
                    return True 
        
        return False

            
        