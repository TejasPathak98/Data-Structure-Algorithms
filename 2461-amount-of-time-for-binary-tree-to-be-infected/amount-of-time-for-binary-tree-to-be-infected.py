# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent_map = {}
        startNode = None

        def dfs_build_parent_map(node):
            nonlocal parent_map,startNode
            if not node:
                return

            if node.val == start:
                startNode = node
            
            if node.left:
                parent_map[node.left] = node
                dfs_build_parent_map(node.left)

            if node.right:
                parent_map[node.right] = node
                dfs_build_parent_map(node.right)

        dfs_build_parent_map(root)

        queue = deque([startNode])
        visited = set()
        visited.add(startNode)
        time = -1

        while queue:

            for _ in range(len(queue)):

                node = queue.popleft()

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if node in parent_map and parent_map[node] not in visited:
                    queue.append(parent_map[node])
                    visited.add(parent_map[node])

            time += 1

        
        return time
                







        

