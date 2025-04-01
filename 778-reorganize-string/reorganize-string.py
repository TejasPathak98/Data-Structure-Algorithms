class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = [(-freq,char) for char,freq in counter.items()]
        heapify(max_heap)

        prev_freq = 0
        prev_char = 0
        result = []

        while max_heap:
            freq,char = heapq.heappop(max_heap)

            result.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq,prev_char))
            
            prev_freq = freq + 1 #decreasing the freq by 1 and adding in next iteration(because we do not want consectuive same characters)
            prev_char = char

        result = "".join(result)

        print(result)

        if len(result) < len(s):
            return ""

        for i in range(1,len(s)):
            if result[i] == result[i - 1]:
                return ""

        return result
