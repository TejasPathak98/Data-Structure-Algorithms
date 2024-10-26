# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append((root,0))
        ans = defaultdict(list)
        res = []

        while queue:
            node,col_idx = queue.popleft()
            ans[col_idx].append(node.val)

            if node.left:
                queue.append((node.left,col_idx - 1))
            
            if node.right:
                queue.append((node.right,col_idx + 1))
        
        low = min(ans.keys())
        high = max(ans.keys())

        for i in range(low,high + 1):
            res.append(ans[i])
        
        return res






        