class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []

        for word , frequency in count.items():
            heap.append([-frequency,word])

        heapq.heapify(heap) 

        return [heapq.heappop(heap)[1] for _ in range(k)]

