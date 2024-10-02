# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        parent = {}
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                top = queue.popleft()

                if top.left:
                    parent[top.left.val] = top
                    queue.append(top.left)
                if top.right:
                    parent[top.right.val] = top
                    queue.append(top.right)
        
        visited = {}
        queue.append(target)

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


                




        