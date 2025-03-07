# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # queue = deque([root])
        # queue.append(None)
        # temp = []
        # final_arr= []

        # while root:
        #     node = queue.popleft()
        #     if node == None:
        #         final_arr.append(temp.copy())
        #         if len(queue) == 0:
        #             break
        #         queue.append(None)
        #     else:
        #         temp.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        
        # return [l[-1] for l in final_arr]
                
        # #O(N) ; O(N)
        if not root:
            return []

        queue = deque([root])
        right_view = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                if i == level_size - 1:
                    right_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_view