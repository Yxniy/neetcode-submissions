# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        def dfs(root, i):
            
            if not root:
                return 

            if len(result) <= i:
                result.append([])
        
            result[i].append(root.val)
            dfs(root.left,i+1)
            dfs(root.right,i+1)
            
            

        dfs(root,0)
        return result