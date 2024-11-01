# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        queue.append(None)
        ans = []
        temp = []

        while queue:
            node = queue.popleft()
            if node == None:
                ans.append(temp.copy())
                temp.clear()
                if len(queue) == 0:
                    break
                queue.append(None)
            else:
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        
        for i,v in enumerate(ans):
            if i % 2 == 1:
                print("Br")
                ans[i] = ans[i][::-1]
        
        return ans

