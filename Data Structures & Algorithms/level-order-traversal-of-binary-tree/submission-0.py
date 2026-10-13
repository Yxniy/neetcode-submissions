# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        alist = []
        h = 0
        def ans(root, level,alist):
            if not root:
                return
            if level == len(alist):
                alist.append([])
            alist[level].append(root.val)
            ans(root.left,level+1,alist)
            ans(root.right,level+1,alist)

        ans(root,h,alist)

        return alist

