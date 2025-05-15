class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        
        while volume:

            curr_height = heights[k]
            fill_index = k

            l = k - 1

            while l >= 0:
                if heights[l] > curr_height:
                    break
                if heights[l] < curr_height: #if we encounter a lower height, we stop there and then change the curr_height, this to ensure that the index gets filled first ahead of others who have same height(which are filled later)
                    curr_height = heights[l]
                    fill_index = l
                l -= 1


            if fill_index == k:
                r = k + 1

                while r < len(heights):
                    if heights[r] > curr_height:
                        break
                    if heights[r] < curr_height:
                        curr_height = heights[r]
                        fill_index = r
                    r += 1

            heights[fill_index] += 1
            volume -= 1

        
        return heights
            

                