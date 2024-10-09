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
        
        queue.append(target)
        visited = {}
        ans = []

        while queue and k > 0:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                visited[node.val] = 1

                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                if node.val in parent and parent[node.val].val not in visited:
                    queue.append(parent[node.val])

            k -= 1
        
        while queue:
            ans.append(queue.popleft().val)
           
        return ans
                
                


        