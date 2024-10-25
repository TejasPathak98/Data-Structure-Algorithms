class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.helper(s,ans,0,"",0)
        return ans
    
    def helper(self,curr,ans,index,temp,count):
        if count > 4:
            return
        if count == 4 and index == len(curr):
            ans.append(temp)
        for i in range(1,4):
            s = curr[index:index + i]
            if index + i > len(curr):
                break
            if (s[0] == "0" and len(s) > 1) or (len(s) == 3 and int(s) >= 256):
                continue
            self.helper(curr,ans,index + i,temp + s + ("." if count < 3 else ""),count + 1)



        