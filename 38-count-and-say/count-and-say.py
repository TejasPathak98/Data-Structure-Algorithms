class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.helper(self.countAndSay(n - 1))
    
    def helper(self,n:string) -> string:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key,gr in groupby(n))