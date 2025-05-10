class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)

        while volume:
            #initial state

            fill = k
            curr_height = heights[k]

            #go left
            l = k - 1

            while l >= 0:
                if heights[l] > curr_height:
                    break
                if heights[l] < curr_height:
                    curr_height = heights[l]
                    fill = l
                l -= 1

            if fill == k:

                r = k + 1
                while r < n:
                    if heights[r] > curr_height:
                        break
                    if heights[r] < curr_height:
                        curr_height = heights[r]
                        fill = r
                    r += 1

            heights[fill] += 1
            volume -= 1

            print(heights,volume)

        
        return heights

            

