class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # 1. Decide if we need to go RIGHT
        # (Check if BOTH p and q are larger than the current root)
        if p.val > root.val and q.val > root.val:
            # The answer is in the right subtree, so return whatever that call finds
            return self.lowestCommonAncestor(root.right, p, q)

        # 2. Decide if we need to go LEFT
        # (Check if BOTH p and q are smaller than the current root)
        elif p.val < root.val and q.val < root.val:
            # The answer is in the left subtree, so return whatever that call finds
            return self.lowestCommonAncestor(root.left, p, q)

        # 3. If neither of the above, we found the split point!
        else:
            return root