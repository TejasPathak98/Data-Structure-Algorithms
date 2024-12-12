class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_arr = []
        max_arr = []
        
        # for arr in arrays:
        #     min_arr.append(arr[0])
        #     max_arr.append(arr[len(arr) - 1])
        
        # ans = float(-inf)

        # for i in range(len(min_arr)):
        #     for j in range(len(max_arr)):
        #         if j == i:
        #             continue
        #         else:
        #             ans = max(ans,abs(min_arr[i] - max_arr[j]))
        
        # return ans

        for i in range(len(arrays)):
            min_arr.append((arrays[i][0],i))
            max_arr.append((arrays[i][len(arrays[i]) - 1],i))
        
        min_arr = sorted(min_arr,key = lambda x : x[0])
        max_arr = sorted(max_arr,key = lambda x : x[0],reverse= True)

        print(min_arr)
        print(max_arr)

        ans = float(-inf)

        i = 0
        j = 0

        while j < len(max_arr):
            if max_arr[j][1] != min_arr[i][1]:
                ans = max(ans,abs(max_arr[j][0] - min_arr[i][0]))
                break
            else:
                j += 1
        
        i = 0
        j = 0

        while i < len(min_arr):
            if max_arr[j][1] != min_arr[i][1]:
                ans = max(ans,abs(max_arr[j][0] - min_arr[i][0]))
                break
            else:
                i += 1
        
        return ans



        