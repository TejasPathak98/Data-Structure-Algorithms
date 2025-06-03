class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #we need the longest subarry with 2 distinct elements

        l = 0
        counter = Counter()
        result = float('-inf')
        k = 2

        for r in range(len(fruits)):
            if counter[fruits[r]] == 0:
                k -= 1
            counter[fruits[r]] += 1

            while k < 0:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    k += 1
                l += 1

            
            result = max(result,(r - l + 1))

        
        return result


