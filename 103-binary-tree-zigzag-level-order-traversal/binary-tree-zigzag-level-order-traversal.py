# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        
        def dfs(root,level):
            if len(ans) == level:
                ans.append([])
            
            if level % 2 == 0:
                ans[level].append(root.val)
            else:
                ans[level].insert(0, root.val)
            
            if root.left:
                dfs(root.left,level + 1)
            if root.right:
                dfs(root.right,level + 1)
        
        dfs(root,0)
        return ans
        
        


        