class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        for i in range(1,10):
            self.dfs(i,n,result)
        
        return result
    
    def dfs(self,x,n,result):
        if x > n:
            return
        result.append(x)

        for i in range(10):
            y = x*10 + i
            if y <= n:
               self. dfs(y,n,result)
    
        