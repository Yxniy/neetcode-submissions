class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. Base Case: If subRoot is None, it technically matches anything (or define per problem rules)
        if not subRoot: return True
        
        # 2. Base Case: If root is None (but subRoot wasn't), we failed to find it
        if not root: return False
        
        # 3. Helper Function (SameTree) - YOUR CODE IS GOOD HERE
        def sameTree(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        # 4. The Logic Glue
        # Check if they are the same tree HERE
        if sameTree(root, subRoot):
            return True
        
        # 5. If not same here, check the children
        # Return True if found in Left OR found in Right
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)