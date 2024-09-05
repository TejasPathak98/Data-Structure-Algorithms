# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(root,path,sum):
            if root is None:
                return [] 
            
            sum += root.val 
            path.append(root.val)

            if root.left is None and root.right is None:
                if sum == targetSum:
                    ans.append(path.copy())
            
            dfs(root.left,path,sum)
            dfs(root.right,path,sum)

            path.pop()
        
        dfs(root,[],0)

        return ans

        