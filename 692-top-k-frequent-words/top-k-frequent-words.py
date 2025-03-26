class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # counter = Counter(words)
        # min_heap = []

        # for word,freq in counter.items():
        #     heapq.heappush(min_heap, (freq,word))

        #     if len(min_heap) > k:
        #         heapq.heappop(min_heap)

        # result = []

        # while min_heap:
        #     ferq,word = heapq.heappop(min_heap)
        #     result.append(word)
        
        # return result[::-1]

        # counter = Counter(words)
        # max_heap = [(-freq,word) for word,freq in counter.items()]
        # heapify(max_heap)
        # result = []

        # for _ in range(k):
        #     result.append(heapq.heappop(max_heap)[1])
        
        # return result

        #O(N + klogN)

        counter = Counter(words)

        return nsmallest(k, counter.keys() ,key = lambda x : (-counter[x],x))

