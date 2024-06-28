class Solution:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(int) 

        for i in s:
            dic[i] = dic[i] + 1

        sorted_dic = sorted(dic.items(), key = lambda item:item[1], reverse= True)

        print(sorted_dic)

        s = ""

        for key,value in sorted_dic:
            for i in range(value):
                s = s + key 

        return s
        