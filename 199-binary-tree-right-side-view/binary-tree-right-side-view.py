# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return root
        ans = []
        temp = []
        res = []

        queue = deque([root])
        queue.append(None)

        while queue:
            node = queue.popleft()
            if node is None:
                if len(queue) == 0:
                    ans.append(temp.copy())
                    break
                else:
                    ans.append(temp.copy())
                    queue.append(None)
                    temp.clear()
            else:
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        for arr in ans:
            res.append(arr[-1])
        
        return res


        