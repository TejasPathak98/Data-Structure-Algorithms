class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        split_logs = []
        number_logs = []
        char_logs = []
        ans = []

        for log in logs:
            split_logs.append(log.split(" ")) #confim this
            if split_logs[-1][1].isnumeric():
                number_logs.append(split_logs[-1])
            else:
                char_logs.append(split_logs[-1])

        char_logs.sort(key = lambda x : (x[1:],x[0]))
        
        
        for log in char_logs:
            ans.append(" ".join(log))
        for log in number_logs:
            ans.append(" ".join(log))
        
        return ans
        