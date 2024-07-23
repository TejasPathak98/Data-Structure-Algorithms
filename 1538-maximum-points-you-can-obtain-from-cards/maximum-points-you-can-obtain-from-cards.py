class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == 0 or not cardPoints:
            return 0 
        
        if k == len(cardPoints):
            return sum(cardPoints)
        
        max_score = 0
        
        curr_sum = sum(cardPoints[:k])
        max_score = curr_sum 

        for i in range(1, k + 1):
            curr_sum = curr_sum - cardPoints[k - i] + cardPoints[-i]
            max_score = max(max_score,curr_sum) 
        
        return max_score
