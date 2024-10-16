# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        dic = defaultdict(int)

        def dfs(root,depth):
            if not root:
                return
            
            dic[depth] = root.val
            dfs(root.left,depth + 1)
            dfs(root.right, depth + 1)
        
        if root:
            dfs(root,0)
        return [dic[i] for i in dic.keys()]

        #O(nlogn) ; O(n)
        


        