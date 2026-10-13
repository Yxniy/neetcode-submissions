# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level = 0
        def dfs(root,ans,level):
            if not root:
                return
            
            if level == len(ans):
                ans.append(root.val)

            dfs(root.right,ans,level+1)
            dfs(root.left,ans,level+1)
        
        dfs(root,ans,level)

        return ans