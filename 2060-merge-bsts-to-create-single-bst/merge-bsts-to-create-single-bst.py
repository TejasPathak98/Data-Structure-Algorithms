# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        root_map = {tree.val : tree for tree in trees} #map for getting the relationship between the root_val and the tree
        count = defaultdict(int) # to store counts of all the node in all trees

        for tree in trees:
            if tree.left:
                count[tree.left.val] += 1
            if tree.right:
                count[tree.right.val] += 1
            count[tree.val] += 1
        
        root = None
        
        for tree in trees: # For finding our ultimate root,the combined root, whose occurence can only be singular
            if count[tree.val] == 1:
                root = tree
                break

        
        def dfs(node): #for merging the trees according to the root_map
            if not node:
                return None

            if not node.left and not node.right and node.val in root_map and node != root_map[node.val]:
                #this is for leaf nodes, where we will merging the other tree
                merge_tree = root_map.pop(node.val) #popping the other tree
                node.left = merge_tree.left
                node.right = merge_tree.right
            dfs(node.left)
            dfs(node.right)

        if root is None:
            return None

        dfs(root)

        def isValidBST(node,Min,Max): #For validating the final tree formed
            if not node:
                return True
            
            if node.val <= Min or node.val >= Max:
                return False
            
            return isValidBST(node.left,Min,node.val) and isValidBST(node.right,node.val,Max)
            
        if len(root_map) > 1:
            return None
        
        if isValidBST(root,float("-inf"),float("inf")):
            return root
        else:
            return None

            


