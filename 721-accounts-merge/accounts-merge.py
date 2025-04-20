class UnionFind:
    def __init__(self,N):
        self.parents = list(range(N))
    def find(self,x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self,child,parent):
        self.parents[self.find(child)] = self.find(parent)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        email_to_user_mapping = {}

        for idx,(_,*emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_user_mapping:
                    uf.union(idx, email_to_user_mapping[email])
                email_to_user_mapping[email] = idx
            
        
        user_to_email_mapping = defaultdict(list)

        for email,user in email_to_user_mapping.items():
            user_to_email_mapping[uf.find(user)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i,emails in user_to_email_mapping.items()]


        