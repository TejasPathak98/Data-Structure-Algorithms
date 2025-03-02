class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, speed in sorted(zip(position,speed),reverse= True):
            distance = target - pos
            time = distance / speed

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
            
        return len(stack)
        