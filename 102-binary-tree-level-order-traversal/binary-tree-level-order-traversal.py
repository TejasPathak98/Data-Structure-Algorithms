# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        
        # queue = deque([root])
        # ans = []

        # while queue:
        #     temp = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()

        #         temp.append(node.val)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     ans.append(temp)

        # return ans

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
        return list(ans.values())



