# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        queue.append(None)
        ans = []
        temp = []

        while queue:
            node = queue.popleft()
            if node is None:
                ans.append(temp.copy())
                temp.clear()
                if len(queue) == 0:
                    break
                else:
                    queue.append(None)
            else:
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        print(ans)
                
        for i,arr in enumerate(ans):
            if i % 2 == 0:
                print(arr)
                for j in range(1,len(arr)):
                    if arr[j - 1] >= arr[j]:
                        return False
                    if arr[j] % 2 == 0:
                        return False
                if arr[0] % 2 == 0:return False
            else:
                print(arr)
                for j in range(1,len(arr)):
                    if arr[j - 1] <= arr[j]:
                        return False
                    if arr[j] % 2 == 1:
                        return False
                if arr[0] % 2 == 1:return False
        
        return True


        