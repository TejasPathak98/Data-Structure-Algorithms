class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s.reverse()
        i = 0
        while i < len(s):
            j = i 
            while j < len(s) and s[j] != ' ':
                j += 1
            left,right = i, j - 1

            while left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            
            i = j + 1
        