class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0

        for i in range(len(digits)):
            num += digits[i] * (10 ** (len(digits) - i - 1))
        
        num += 1

        new_digits = []

        while num > 0:
            new_digits.append(num % 10)
            num = num // 10

        return new_digits[::-1]

        