# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def dfs(node, maxi):
            nonlocal result
            if not node:
                return 
            
            if node.val >= maxi:
                result+=1
                maxi = max(node.val,maxi)
            
            dfs(node.left,maxi)
            dfs(node.right,maxi)
        
        dfs(root,root.val)

        return result