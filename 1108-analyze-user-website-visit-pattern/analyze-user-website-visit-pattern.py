class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = []

        for i in range(len(username)):
            data.append((username[i],timestamp[i],website[i]))

        data.sort(key = lambda x : x[1])

        user_to_website_mapping = defaultdict(list)

        for user,_,website in data:
            user_to_website_mapping[user].append(website)
        
        websitePattern_to_users_mapping = defaultdict(list)

        for user,websites in user_to_website_mapping.items():
            if len(websites) < 3:
                continue
            website_patterns = set(combinations(websites,3))
            for pattern in website_patterns:
                websitePattern_to_users_mapping[pattern].append(user)

        
        best_pattern = None
        no_of_users = 0

        for pattern,list_users in websitePattern_to_users_mapping.items():
            score  = len(list_users)
            if score > no_of_users or (no_of_users == score and (pattern < best_pattern or pattern is None)):
                best_pattern = pattern
                no_of_users = score
            
        
        return best_pattern
        


