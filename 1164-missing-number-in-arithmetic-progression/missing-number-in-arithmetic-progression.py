class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = []

        if all(x == arr[0] for x in arr):
            return arr[0]

        for i in range(1,n):
            diff.append(abs(arr[i] - arr[i - 1]))
        
        the_diff = float('inf')
        min_diff = float('inf')
        max_diff = float('-inf')
        f = Counter(diff)

        
        for x,freq in f.items():
            if freq >= 2:
                the_diff = x
                break
            max_diff = max(max_diff,x)
            min_diff = min(min_diff,x)
        
        if the_diff != float('inf'):
            for i in range(1,n):
                if abs(arr[i] - arr[i - 1]) > the_diff:
                    if arr[i] > arr[i - 1]:
                        print(the_diff)
                        return arr[i - 1] + the_diff
                    else:
                        return arr[i - 1] - the_diff
        else:
            for i in range(1,n):
                if abs(arr[i] - arr[i - 1]) == max_diff:
                    if arr[i] > arr[i - 1]:
                        return arr[i - 1] + min_diff
                    else:
                        return arr[i - 1] - min_diff



        


        