class Solution:
    def jump(self, nums: List[int]) -> int:
        currFar = 0
        currEnd = 0

        if len(nums) == 1:
            return 0

        prev = list(range(len(nums)))

        jumps = 0

        i = 0

        for i in range(len(nums)):
            if i + nums[i] > currFar:
                currFar = i + nums[i]

                for j in range(i + 1,min(currFar + 1,len(nums))):
                    prev[j] = i
 
            if i == currEnd:
                currEnd = currFar
                jumps += 1

                if currEnd >= len(nums) - 1:
                    temp = []
                    curr = len(nums) - 1

                    temp.append(len(nums) - 1)

                    while curr != 0:
                        curr = prev[curr]
                        temp.append(curr)
                    
                    print(temp)
                    return jumps

