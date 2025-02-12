class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        the_sum = 0

        for i in range(n - 1,-1,-1):
            the_sum += digits[i] * (10 ** ((n - 1) - i))
        
        the_sum += 1

        temp = []

        while the_sum:
            temp.append(the_sum % 10)
            the_sum = the_sum // 10
        
        temp = temp[::-1]

        return temp

        