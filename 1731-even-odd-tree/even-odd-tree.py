# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        q = deque([root])
        #q.append(None) 
        res = []

        while q:
            size = len(q)
            temp = []

            for _ in range(size):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(temp)
            
        for i in range(len(res)):
            if i % 2 == 0:
                temp = res[i]
                for j in range(len(temp)):
                    if temp[j] % 2 == 0:
                        return False
                    if j > 0 and temp[j - 1] >= temp[j]:
                        return False
                
            else:
                temp = res[i]
                for j in range(len(temp)):
                    if temp[j] % 2 == 1:
                        return False
                    if j > 0 and temp[j - 1] <= temp[j]:
                        return False
        
        return True






        