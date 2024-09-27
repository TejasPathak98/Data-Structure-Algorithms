# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        my_dict = defaultdict(list)

        def dfs(root,level):
            if root is None:
                return
            
            my_dict[level].append(root.val)

            dfs(root.left,level +1)
            dfs(root.right,level + 1)
        
        dfs(root,0)

        for level,arr in my_dict.items():
            ans.append(arr)
        
        return ans

        