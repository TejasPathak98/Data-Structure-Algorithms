# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_dict = defaultdict(list)

    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        
        # ans = []
        # queue = deque([root])
        # temp = []

        # while queue:
        #     size = len(queue)
        #     ans.append(temp.copy())
        #     temp.clear()
        #     for _ in range(size):
        #         node = queue.popleft()
        #         temp.append(node.val)

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        
        # ans.append(temp)
        # return ans[1:]

        # #O(N) ; O(N)
        if not root:
            return []
        
        self.dfs(root,0)
        return list(self.node_dict.values())

    def dfs(self,root,level):
        if root is None:
            return

        self.node_dict[level].append(root.val)

        if root.left:
            self.dfs(root.left,level + 1)
        if root.right:
            self.dfs(root.right,level + 1)





    



