# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #For Every dfs path, the number of cameras on that path is equal to the number of nodes on that path // 2 , but the cameras are common for some paths

        # if not root:
        #     return 0
        
        # if not root.left and not root.right:
        #     return 1
        
        # queue = deque([root])
        # cameras = 0
        # levels = []

        # while queue:
        #     no_of_nodes = 0 

        #     for _ in range(len(queue)):
        #         node = queue.popleft()

        #         no_of_nodes += 1

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
                
        #     levels.append(no_of_nodes)

        # if len(levels) == 2:
        #     return min(levels[0],levels[1])

        # cameras_1 = cameras_2 = 0

        # if len(levels) % 2 == 0:
        #     for i in range(len(levels)):
        #         if i % 2 == 0:
        #             cameras_1 += levels[i]
        #         else:
        #             cameras_2 += levels[i]
        #         cameras = min(cameras_1,cameras_2)
        # else:
        #     for i in range(len(levels)):
        #         if i % 2 == 1:
        #             cameras += levels[i]

        
        # return cameras


        #DFS Post-Order Traversal

        self.cameras = 0

        #0 -> needs a camera
        #1 -> Has a camera
        #2 -> is covered

        def dfs(node):
            if not node:
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0: #the child need a camera
                self.cameras += 1
                return 1 #it has a camera
            
            if left ==1 or right ==1: #child has a camera
                return 2 #its convered

            
            return 0 #now it needs a camera(becase left == 2 or right == 2)
        

        if dfs(root) == 0:
            self.cameras += 1
        
        return self.cameras


        
        

        


        




            