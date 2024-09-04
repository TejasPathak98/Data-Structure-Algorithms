# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return
        
        ans = []
        f = []

        queue = deque([root])
        queue.append(None)

        while queue:
            x = queue.popleft()
            if x == None:
                f.append(ans.copy())
                ans.clear()
                if len(queue) == 0:
                    break
                queue.append(None)
                continue
            else:
                ans.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
        
        return f

            





        