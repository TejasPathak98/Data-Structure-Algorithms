class Solution:
    def reorganizeString(self, s: str) -> str:
        
        result = []
        counter= Counter(s)
        max_heap = [(-freq,char) for char,freq in counter.items()]
        heapify(max_heap)

        prev_char = None
        prev_freq = 0 

        while max_heap:

            freq,char = heapq.heappop(max_heap)

            result.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq,prev_char))
            
            prev_freq = freq + 1
            prev_char = char

        
        result = "".join(result)

        if len(result) < len(s):
            return ""

        return result


            


