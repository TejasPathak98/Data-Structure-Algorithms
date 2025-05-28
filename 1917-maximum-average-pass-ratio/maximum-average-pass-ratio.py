class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        #the idea is here that we calculate the gain of one student in each class and put that into a max heap, so the first gain goes to 
        #the most needed class(or highest gain) and we do that till we finish all the extra students

        def gain(pass_,total):
            return (pass_ + 1)/(total + 1) - (pass_/total)
        
        max_heap = []
        Sum = 0.0

        for pass_,total in classes:
            Sum += (pass_/total)
            heapq.heappush(max_heap, (-gain(pass_,total) , pass_ , total))

        
        for _ in range(extraStudents):
            new_gain , pas , tot = heapq.heappop(max_heap)

            Sum -= pas/tot
            pas += 1
            tot += 1
            Sum += pas / tot
            heapq.heappush(max_heap, (-gain(pas,tot) , pas , tot))
        

        return Sum / len(classes)

        #O(NlogN) ; O(N)




        

