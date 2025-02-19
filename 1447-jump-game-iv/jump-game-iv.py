class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:return 0
        
        # min_steps = float("inf")
        # #visited = set()

        the_dict = defaultdict(list)
        for i in range(len(arr)):
            the_dict[arr[i]].append(i)

        # def helper(pos,visited,steps):
        #     nonlocal min_steps,the_dict
        #     if pos < 0 or pos >= len(arr) or pos in visited:
        #         return
            
        #     visited.add(pos)

        #     if pos == len(arr) - 1:
        #         min_steps = min(min_steps,steps)
        #         return
            
        #     helper(pos + 1,visited,steps + 1)
        #     helper(pos - 1,visited,steps + 1)

        #     for index in the_dict[arr[pos]]:
        #         if index != pos and index not in visited:
        #             helper(index,visited,steps + 1)
        #     the_dict[arr[pos]] = []
        
        # helper(0,set(),0)

        # return min_steps
    
        queue = deque()
        queue.append(0)
        steps = -1
        visited = set()


        while queue:
            steps += 1
            for _ in range(len(queue)):
                index = queue.popleft()

                if index == len(arr) - 1:
                    return steps

                if index in visited:
                    continue
                
                visited.add(index)
                
                if index + 1 < len(arr):
                    queue.append(index + 1)
                if index - 1 >=0:
                    queue.append(index - 1)
                
                for i in the_dict[arr[index]]:
                    if i != index and i not in visited:
                        queue.append(i)
                the_dict[arr[index]] = []
        
        return -1
                






