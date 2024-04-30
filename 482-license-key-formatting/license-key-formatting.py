class Solution:
    @staticmethod
    def helper(st,char,k):
        chunks = [st[i:i + k] for i in range(0,len(st),k)]
        result = char.join(chunks)
        return result
    
    
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-","").upper()
        re = len(s)%k 
        
        if re == 0:
            formatted_length_first = k 
        else:
            formatted_length_first = re  
        
        fs = s[:formatted_length_first]
        ss = s[formatted_length_first:] 

        rest = self.helper(ss,"-",k) if ss else "" 

        if rest:
            return fs + "-" + rest 
        else:
            return fs 
        

    
    

            

