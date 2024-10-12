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
        dic = defaultdict(list)
        ans = []

        while queue:
            node,column_pos = queue.popleft()
            dic[column_pos].append(node.val)

            if node.left:
                queue.append((node.left,column_pos - 1))
            if node.right:
                queue.append((node.right,column_pos + 1))
        
        dic_sorted = dict(sorted(dic.items(), key = lambda x : x[0]))
        for col_pos,val in dic_sorted.items():
            ans.append(val)
        
        return ans

            
            
        