class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        #Similar to permutations

        result = [0] * (2*n - 1)
        used = [False] * (n + 1)
        self.backtrack(result,used,n,0)
        return result


    def backtrack(self,result,used,n,idx):
        while idx < 2* n - 1 and result[idx] > 0:
            idx += 1
        if idx == 2* n - 1:
            return True
        
        for i in range(n,0,-1):
            if used[i]:
                continue

            if i == 1:
                used[1] = True
                result[idx] = 1
                if self.backtrack(result,used,n,idx + 1):
                    return True
                used[1] = False
                result[idx] = 0
            else:
                if idx + i < 2*n - 1 and result[idx + i] == 0:
                    used[i] = True
                    result[idx] = i
                    result[i + idx] = i
                    if self.backtrack(result,used,n,idx + 1):
                        return True 
                    used[i] = False
                    result[idx] = 0
                    result[i + idx] = 0

    

