# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(x,y,direction):

            if (x,y) in visited:
                return
            
            visited.add((x,y))
            robot.clean()

            for i,(dx,dy) in enumerate((directions[direction:]  + directions[:direction])):
                x_ = x + dx
                y_ = y + dy

                if robot.move():
                    dfs(x_,y_,(direction + i) % 4)

                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnLeft()
                else:
                    robot.turnRight()

        
        dfs(0,0,0)



            




