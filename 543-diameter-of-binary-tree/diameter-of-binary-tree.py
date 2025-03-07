# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_diameter 

    # def dfs(self,root):
    #     if not root:
    #         return
        
    #     self.max_diameter = max(self.max_diameter,self.depth(root.left) + self.depth(root.right))

    #     self.dfs(root.left)
    #     self.dfs(root.right)

    # def depth(self,root):
    #     if root is None:
    #         return 0
        
    #     return 1 + max(self.depth(root.left),self.depth(root.right))


    def dfs(self,root):
        if root is None:
            return 0

        left_depth = self.dfs(root.left)
        right_depth = self.dfs(root.right)

        self.max_diameter = max(self.max_diameter,left_depth + right_depth)

        return 1 + max(left_depth,right_depth)
        

    




        
