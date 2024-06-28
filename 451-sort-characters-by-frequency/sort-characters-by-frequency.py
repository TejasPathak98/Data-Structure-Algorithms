class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}

        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1 
            else:
                dic[s[i]] += 1
        
        sorted_dic = sorted(dic.items(), key = lambda item:item[1], reverse= True)

        print(sorted_dic)

        s = ""

        for key,value in sorted_dic:
            for i in range(value):
                s = s + key 

        return s
        