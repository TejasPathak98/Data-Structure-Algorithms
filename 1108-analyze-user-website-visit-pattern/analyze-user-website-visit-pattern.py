from collections import defaultdict
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = [(username[i],timestamp[i],website[i]) for i in range(len(username))]
        #Aggregating

        data = sorted(data,key = lambda x : x[1]) #Sorting by timestamp

        visits_per_user = defaultdict(list)

        for user,timestamp,website in data:
            visits_per_user[user].append(website)
        
        patterns_mapping_to_users = defaultdict(list)

        print(visits_per_user)

        for user,websites in visits_per_user.items():
            if len(websites) < 3:
                continue
            
            website_patterns = set(combinations(websites, 3))
            print(website_patterns)
            for pattern in website_patterns:
                patterns_mapping_to_users[pattern].append(user)

        print(patterns_mapping_to_users)
        
        max_score = 0
        best_pattern = None

        for pattern,users in patterns_mapping_to_users.items():
            score = len(users)
            print(score)
            if score > max_score or (max_score == score and (best_pattern is None or pattern < best_pattern)):
                best_pattern = pattern
                max_score = score

        print(best_pattern)

        return list(best_pattern)
