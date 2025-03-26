class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes,key = lambda x : x[1], reverse=True)
        ans = 0
        i = 0

        print(boxTypes)

        while i < len(boxTypes):
            units = boxTypes[i][0] * boxTypes[i][1]
            if boxTypes[i][0] < truckSize:
                ans += units
                truckSize -= boxTypes[i][0]
                i += 1
                print(ans,units,truckSize)
            else:
                no_of_boxes = truckSize
                ans += boxTypes[i][1] * no_of_boxes
                print(ans)
                break
        
        return ans
