# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        queue = deque()
        queue.append((root,0))
        columns = defaultdict(list)

        while queue:

            node,col = queue.popleft()
            columns[col].append(node.val)

            if node.left:
                queue.append((node.left,col - 1))
            if node.right:
                queue.append((node.right,col + 1))
        
        low = min(columns.keys())
        high = max(columns.keys())

        for i in range(low,high + 1):
            ans.append(columns[i])
        
        return ans