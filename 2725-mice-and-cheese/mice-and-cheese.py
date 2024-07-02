class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        heap = [] 

        for i in range(len(reward1)):
            heap.append([reward2[i] - reward1[i],i])
        heapq.heapify(heap) 

        res = 0
        visited = {}
        
        while(k):
            idx = heapq.heappop(heap)[1]
            res += reward1[idx] 
            visited[idx] = 1 
            k -= 1
        
        for i in range(len(reward2)):
            if visited.get(i) != None:
                continue 
            res += reward2[i] 
        
        return res

        