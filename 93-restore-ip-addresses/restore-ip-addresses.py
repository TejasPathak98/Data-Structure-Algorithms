class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.helper(ans,s,0,"",0)
        return ans
    
    def helper(self,ans,s,index,temp,count):
        if count > 4:
            return
        elif count == 4 and index == len(s):
            ans.append(temp)
            return
        else:
            for i in range(1,4):
                curr = s[index:index + i]
                if index + i > len(s):
                    break
                if (curr[0] == "0" and len(curr) > 1) or (len(curr) == 3 and int(curr) >= 256):
                    continue
                self.helper(ans,s,index + i,temp + curr + ("." if count < 3 else ""),count + 1)

                
        