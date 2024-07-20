class Solution:
    
    def __init__(self):
        self.dic = {}

    def helper(self,dic,x,arr):
        count = 0
        for i in range(-50 , 0, 1):
            if dic.get(i,0) > 0:
                count = count + dic.get(i)
            if count >= x:
                return i
        return 0

    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        n = len(nums) 
        neg = 0 
        ans = []
        start = 0
        window_size = 0

        for end in range(n):
            if start > n - k:
                break
            
            if nums[end] < 0:
                neg += 1
                self.dic[nums[end]] = self.dic.get(nums[end],0) + 1
            
            window_size += 1
            if window_size == k:
                temp = 0
                if neg >= x:
                    temp = self.helper(self.dic,x,nums)
                    print("Here")
                    print(temp)
                if nums[start] < 0:
                    self.dic[nums[start]] = self.dic.get(nums[start]) - 1
                ans.append(temp)
                start += 1
                window_size -= 1


        return ans                


            

            



        