class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def SumOfDigits(x):
            Sum = 0
            while x:
                Sum += (x % 10)
                x = x // 10
            return Sum

        groups = defaultdict(list)

        for num in nums:
            DSum = SumOfDigits(num)
            groups[DSum].append(num)

        result = -1

        for val in groups.values():
            if len(val) >= 2:
                largest = heapq.nlargest(2,val)
                result = max(result,largest[0] + largest[1])

        
        return result

        
       






