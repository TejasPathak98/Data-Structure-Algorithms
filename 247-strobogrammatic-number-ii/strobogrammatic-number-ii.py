class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(curr_len,tar_len):
            if curr_len == 0:
                return [""]
            if curr_len == 1:
                return ["0","1","8"]
            
            middles = helper(curr_len - 2,tar_len)
            result = []

            for middle in middles:
                if curr_len != tar_len:
                    result.append("0" + middle + "0")
                result.append("1" + middle + "1")
                result.append("8" + middle + "8")
                result.append("9" + middle + "6")
                result.append("6" + middle + "9")

            return result
        
        return helper(n,n)

        