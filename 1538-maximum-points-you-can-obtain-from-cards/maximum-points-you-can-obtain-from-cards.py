class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints) 
        
        max_sum = sum(cardPoints) 
        subarray_length = len(cardPoints) - k
        subarray_sum = sum(cardPoints[:subarray_length])
        current_sum = subarray_sum

        for i in range(subarray_length,len(cardPoints)):
            current_sum += cardPoints[i] - cardPoints[i - subarray_length]
            subarray_sum = min(subarray_sum,current_sum) 
        
        return sum(cardPoints) - subarray_sum
