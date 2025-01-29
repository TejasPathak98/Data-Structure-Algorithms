# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = defaultdict(list)

        def dfs(node,level):
            if not node:
                return
            
            ans[level].append(node.val)

            if node.left:
                dfs(node.left,level + 1)
            if node.right:
                dfs(node.right,level + 1)

        dfs(root,0)
            
        result = []
        for k,v in ans.items():
            result.append(v)
        return result
            

        