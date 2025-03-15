class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # index_ignore = set()
        
        # for idx,List in enumerate(triplets):
        #     if List[0] > target[0] or List[1] > target[1] or List[2] > target[2]:
        #         index_ignore.add(idx)
        
        counter = [0,0,0]

        for idx,List in enumerate(triplets):
            if List[0] > target[0] or List[1] > target[1] or List[2] > target[2]:
                continue
            else:
                if List[0] == target[0]:
                    counter[0] = 1
                if List[1] == target[1]:
                    counter[1] = 1
                if List[2] == target[2]:
                    counter[2] = 1
            

        if all(counter) == 1:
            return True
        else:
            return False
