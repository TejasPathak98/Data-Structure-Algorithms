class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def neighbor(s):
            i = 0

            while i < len(s):
                if s[i] == s2[i]:
                    i += 1
                else:
                    break
            
            for j in range(i + 1,len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    ls = list(s)
                    ls[j] ,ls[i] = ls[i] , ls[j]
                    yield ''.join(ls)
        
        queue = deque([(s1,0)])
        seen = set()
        seen.add(s1)

        while queue:
            curr,k = queue.popleft()

            if curr == s2:
                return k
            
            for nei in neighbor(curr):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei,k + 1))
        

        return -1
