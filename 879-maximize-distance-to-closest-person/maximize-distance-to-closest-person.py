class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # seated = []
        # non_seated = []

        # for i in range(len(seats)):
        #     if seats[i] == 1:
        #         seated.append(i)
        #     else:
        #         non_seated.append(i)
        
        # seated.sort()
        # non_seated.sort()

        # for pos in seated:

        seated = []
        max_distance = -float('inf')
        p1 = -1
        p2 = -1
        fp = -1

        for i in range(len(seats)):
            if seats[i] == 1:
                seated.append(i)
        
        if len(seated) == 1:
            fp = seated[0]
            return max(fp - 0, len(seats) - 1 - fp)

        for i in range(len(seated) - 1):
            if seated[i + 1] - seated[i] > max_distance:
                max_distance = seated[i + 1] - seated[i]
       

        return max(max_distance // 2,seated[0],len(seats) - 1 - seated[-1])


        


