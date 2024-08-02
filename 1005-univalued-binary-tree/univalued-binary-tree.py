# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def bfs_helper(root,arr):
            if root is None:
                return
            
            q = deque([root])

            while q:
                node = q.popleft()
                arr.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            return
        
        arr = []
        bfs_helper(root,arr)
        if arr[0]*len(arr) == sum(arr):
            return True 
        else:
            return False

        