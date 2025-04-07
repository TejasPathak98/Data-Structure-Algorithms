class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = []

        for i in range(len(timestamp)):
            data.append((username[i],timestamp[i],website[i]))
        
        data = sorted(data, key = lambda x : x[1])

        user_to_website_mapping = defaultdict(list)

        for user,timestamp,website in data:
            user_to_website_mapping[user].append(website)
        
        pattern_to_user_mapping = defaultdict(list)

        for user , websites in user_to_website_mapping.items():
            if len(websites) < 3:
                continue
            patterns = set(combinations(websites, 3))
            for pattern in patterns:
                pattern_to_user_mapping[pattern].append(user)
        

        best_pattern = None
        best_score = 0

        for pattern,users in pattern_to_user_mapping.items():
            score = len(users)
            if score > best_score or (score == best_score and (best_pattern == None or pattern < best_pattern)):
                best_score = score
                best_pattern = pattern
            
        
        return best_pattern