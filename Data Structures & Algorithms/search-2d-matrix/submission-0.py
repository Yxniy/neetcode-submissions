class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False # Safety check
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        # Fix #2: Subtract 1 for 0-based indexing
        right = (rows * cols) - 1
        
        while left <= right:
            # Fix #3: Standard binary search mid formula
            mid = (left + right) // 2
            
            # Fix #4: Divide by COLS to get row, Modulo by COLS to get col
            mid_val = matrix[mid // cols][mid % cols]
            
            if mid_val == target:
                return True
            # Fix #5: If value is too small, move right (increase left)
            elif mid_val < target:
                left = mid + 1
            # Fix #5: If value is too big, move left (decrease right)
            else:
                right = mid - 1
                
        return False