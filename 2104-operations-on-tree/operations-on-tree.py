class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = defaultdict(list)
        for i,p in enumerate(parent):
            if p != -1:
                self.children[p].append(i)
        self.locked = {}
        

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            del self.locked[num]
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        
        #looking for locked ancestors

        curr = num

        while curr != -1:
            if curr in self.locked:
                return False
            curr = self.parent[curr]
        
        #checking children

        locked_children = []

        def dfs(node):
            if node in self.locked:
                locked_children.append(node)
            for child in self.children[node]:
                dfs(child)

        dfs(num)

        if not locked_children:
            return False

        
        for child in locked_children:
            del self.locked[child]
        

        self.locked[num] = user
        return True

        

        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)