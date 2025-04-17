class UnionFind:
    def __init__(self,N):
        self.parents = list(range(N))
    def find(self,x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    def union(self,child,parent):
        self.parents[self.find(child)]  =self.find(parent)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        email_to_owner = {}

        for i,(_,*emails) in enumerate(accounts):
            for email in emails:
                if email in email_to_owner:
                    uf.union(i, email_to_owner[email])
                email_to_owner[email] = i
        

        owner_to_email = defaultdict(list)

        for email,owner in email_to_owner.items():
            owner_to_email[uf.find(owner)].append(email)

        
        return [[accounts[i][0]] + sorted(emails) for i,emails in owner_to_email.items()]

        