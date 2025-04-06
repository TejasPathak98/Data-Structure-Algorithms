class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        temp = []        

        i = 0

        while i < len(asteroids) - 1:
            x = asteroids[i]
            y = asteroids[i + 1]

            if x*y > 0 or (x < 0 and y > 0):
                i += 1
                continue
            else:
                if abs(x) == abs(y):
                    asteroids[i] = 2000
                    asteroids[i + 1] = 2000
                    i += 2
                    continue
                else:
                    if abs(x) > abs(y):
                        asteroids[i + 1] = 2000
                    else:
                        asteroids[i] = 2000
                    i += 2
                    continue

        
        for i in range(len(asteroids)):
            if asteroids[i] == 2000:
                continue
            else:
                temp.append(asteroids[i])
        
        print(temp)

        
        if all(x > 0 for x in temp) > 0 or all(x < 0 for x in temp) < 0 or len(temp) == len(asteroids):
            print("br")
            return temp
        
        else:
            return self.asteroidCollision(temp)

