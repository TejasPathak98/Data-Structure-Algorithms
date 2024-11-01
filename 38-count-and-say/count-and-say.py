class Solution:
    def countAndSay(self, n: int) -> str:
        string = '1'

        for _ in range(n - 1):
            string = Solution.helper(string)
        
        return string
    
    @staticmethod
    def helper(n:string) -> string:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key,gr in groupby(n))

    
        