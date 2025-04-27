# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        col_dict = defaultdict(list)

        def dfs(node,row,col):
            if not node:
                return
            
            col_dict[col].append((row,node.val))

            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        

        dfs(root,0,0)

        answer = []

        for col in sorted(col_dict.keys()):
            col_dict[col].sort(key = lambda x : (x[0] , x[1]))
            answer.append([val for row,val in col_dict[col]])

        
        return answer
