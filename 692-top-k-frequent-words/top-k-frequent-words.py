class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        
        counter = Counter(words)

        max_heap = []
        heapify(max_heap)
        
        for word,freq in counter.items():
            heapq.heappush(max_heap, (-freq,word))

        res = []

        for _ in range(k):
            _,word = heapq.heappop(max_heap)
            res.append(word)

        
        return res

        

