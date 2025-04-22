# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        nodes_dict = defaultdict(list)

        def dfs(node,row,col):
            if not node:
                return None

            nodes_dict[col].append((row,node.val))
            
            dfs(node.left,row + 1,col - 1)
            dfs(node.right,row +1,col + 1)
        
        dfs(root,0,0)

        result = []

        for col in sorted(nodes_dict.keys()):
            nodes_dict[col].sort(key = lambda  x : (x[0],x[1]))
            result.append([val for key,val in nodes_dict[col]])
        
        return result
            
