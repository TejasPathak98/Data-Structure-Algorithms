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

        columns = defaultdict(list)
        queue = []
        queue.append((root,0))

        while len(queue):
            node,col = queue.pop(0)
            columns[col].append(node.val)

            if node.left:
                queue.append((node.left,col - 1))
            if node.right:
                queue.append((node.right,col + 1))
        
        low = min(columns.keys())
        high = max(columns.keys())
        ans = []

        for i in range(low,high + 1):
            ans.append(columns.get(i))

        return ans
        
        