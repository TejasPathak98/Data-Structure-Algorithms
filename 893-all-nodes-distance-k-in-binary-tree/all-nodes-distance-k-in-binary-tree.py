# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        queue = deque([root])
        parent = {}

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
                parent[node.left.val] = node
            if node.right:
                queue.append(node.right)
                parent[node.right.val] = node
        

        queue = deque([target])
        visited = set()
        visited.add(target)
        ans = []

        while queue and k > 0:
            size = len(queue)

            for _ in range(size):

                node = queue.popleft()

                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                if node.val in parent and parent[node.val] not in visited:
                    queue.append(parent[node.val])
                    visited.add(parent[node.val])
            
            k -= 1

        while queue:
            ans.append(queue.pop().val)
        
        return ans
            