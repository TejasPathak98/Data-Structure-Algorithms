class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        x = 0
        l = 0
        r = len(people) - 1
        people.sort()

        while l <= r:
            x += 1

            if people[l] + people[r] <= limit:
                l += 1
            
            r -= 1

        return x

        #its greedy approach, take the first individual and then the last...the lightest and then the heaviest...




