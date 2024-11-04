# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                parent[node.left.val] = node
                queue.append(node.left)
            if node.right:
                parent[node.right.val] = node
                queue.append(node.right)
        
        ans = []
        queue = deque([target])
        visited = {}

        while queue and k > 0:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                visited[node] = True

                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                if node.val in parent and parent[node.val] not in visited:
                    queue.append(parent[node.val])

            k -= 1

        while queue:
            ans.append(queue.pop().val)
        
        return ans





        