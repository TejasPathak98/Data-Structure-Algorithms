# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        queue = deque([root])
        queue.append(None)
        ans = []
        temp = []

        while queue:
            node = queue.popleft()
            if node is None:
                ans.append(temp.copy())
                temp.clear()
                if len(queue) == 0:
                    break
                else:
                    queue.append(None)
            else:
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans
            
