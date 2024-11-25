class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        lookup = defaultdict(list)

        for cid,parent_id in zip(pid,ppid):
            lookup[parent_id].append(cid)
        
        dq = deque([kill])
        res = []

        while dq:
            id = dq.popleft()
            if id in lookup:
                dq.extend(lookup[id])
            res.append(id)
        
        return res
        