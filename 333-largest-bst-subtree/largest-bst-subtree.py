# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if root is None:
                return float('inf'),float('-inf'),True,0
        
            lmin,lmax,l,lsize = dfs(root.left)
            rmin,rmax,r,rsize = dfs(root.right)

            size = lsize + rsize + 1
            is_Bst = False
            if lmax < root.val < rmin and l and r:
                is_Bst = True
            if is_Bst:
                self.res = max(self.res,size)
            
            return min(lmin,rmin,root.val) , max(lmax,rmax,root.val) , is_Bst ,size
        
        dfs(root)
        return self.res

        