class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        sequence = "1"
        t = 0
        fs = ""
        

        def helper(sequence):
            nonlocal t,fs
            t += 1
            if t == n:
                fs = sequence
                return
            
            temp = ""
            cnt = 1
            i = 0

            if len(sequence) == 1:
                temp = "11"
            else:
                while i <= len(sequence) - 1:
                    while i < len(sequence) - 1 and sequence[i] == sequence[i + 1]:
                        cnt += 1
                        i += 1
                    temp = temp + str(cnt) + str(sequence[i])
                    cnt = 1
                    i += 1
            print(temp)
            helper(temp)
        
        helper(sequence)
        return fs
        



       
            
            



        