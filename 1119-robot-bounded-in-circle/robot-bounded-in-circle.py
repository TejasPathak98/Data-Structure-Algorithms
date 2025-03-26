class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if len(set(instructions)) == 1 and "G" in set(instructions):
            return False
        
        ix = x = 0
        iy = y = 0
        direction = 1  #(1 - N, 2 - S , 3 - E , 4 - W)

        for _ in range(4):
            for ch in instructions:
                if ch == "G":
                    if direction == 1:
                        y += 1
                    elif direction == 2:
                        y -= 1
                    elif direction == 3:
                        x += 1
                    else:
                        x -= 1
                elif ch == "L":
                    if direction == 1:
                        direction = 4
                    elif direction == 2:
                        direction = 3
                    elif direction == 3:
                        direction = 1
                    elif direction == 4:
                        direction = 2
                else:
                    if direction == 1:
                        direction = 3
                    elif direction == 2:
                        direction = 4
                    elif direction == 3:
                        direction = 2
                    elif direction == 4:
                        direction = 1

            
        if ix == x and iy == y:
            return True

        return False