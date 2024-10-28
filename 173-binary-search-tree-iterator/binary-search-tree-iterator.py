# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.ptr = 0
        def helper(root):
            if not root:
                return
            helper(root.left)
            self.arr.append(root.val)
            helper(root.right)
        helper(root)
        
    def next(self) -> int:
        val = self.arr[self.ptr]
        self.ptr += 1
        return val
        
    def hasNext(self) -> bool:
        if self.ptr <= len(self.arr) - 1:
            return True
        else:
            return False

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()