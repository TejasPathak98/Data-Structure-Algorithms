class Solution:
    def countAndSay(self, n: int) -> str:
        String = '1'

        for _ in range(n - 1):
            String = self.helper(String)
        
        return String
    
    #@staticmethod
    def helper(self,n:string) -> string:
        return ''.join(f'{sum(1 for _ in gr)}{key}' for key,gr in groupby(n))


        