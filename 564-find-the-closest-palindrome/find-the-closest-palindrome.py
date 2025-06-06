class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def generate_palindrome(prefix,isEven):
            s = str(prefix)
            if isEven:
                return int(s + s[::-1])
            else:
                return int(s + s[-2::-1])
            
        if len(n) == 1:
            return str(int(n) - 1)
        
        length = len(n)
        number = int(n)
        prefix = int(n[:(length + 1) // 2])

        candidates = {
            10**(length - 1) - 1,
            10**length + 1,
            generate_palindrome(prefix - 1,length % 2 == 0),
            generate_palindrome(prefix,length % 2 == 0),
            generate_palindrome(prefix + 1,length % 2 == 0)
        }

        candidates.discard(number)

        return str(min(candidates,key = lambda x : (abs(x - number) , x)))


        
