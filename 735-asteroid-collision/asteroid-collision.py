class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]: #negative asteroid found and top of stack in positive
                if stack[-1] < -asteroid:
                    stack.pop() #The +ve value is popped out
                    continue # we continue to match with remaining asteroids
                elif stack[-1] == -asteroid:
                    stack.pop() #Both are same size , both expplode
                break
            else:
                stack.append(asteroid) # for positive asteroid and for negative asteroid who have beaten all the +Ve ones and gotten here from continue(basically those which have skipped the break)

        
        return stack
