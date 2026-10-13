class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # Global variable to store the best answer
        
        def height(node):
            if not node:
                return 0
            
            # 1. Recursively find the height of left and right subtrees
            left_h = height(node.left)
            right_h = height(node.right)
            
            # 2. Calculate diameter passing through THIS node
            # Diameter = Left Height + Right Height
            current_diameter = left_h + right_h
            
            # 3. Update the global maximum if this path is bigger
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # 4. Return the HEIGHT to the parent
            # Height = 1 (this node) + the taller child
            return 1 + max(left_h, right_h)
        
        height(root)
        return self.max_diameter