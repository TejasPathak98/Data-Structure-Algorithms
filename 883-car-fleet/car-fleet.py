class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos , v in sorted(zip(position,speed),reverse=True):
            dis = target - pos
            time = dis / v

            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        
        return len(stack)

        