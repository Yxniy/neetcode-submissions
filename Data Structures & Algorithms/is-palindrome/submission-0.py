class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # 1. Move Left pointer forward until we find a letter/number
            # We must check left < right again to prevent going out of bounds
            while left < right and not s[left].isalnum():
                left += 1
                
            # 2. Move Right pointer backward until we find a letter/number
            while left < right and not s[right].isalnum():
                right -= 1
            
            # 3. Compare characters (Case insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # 4. Success! Move both inward for the next round
            left += 1
            right -= 1
            
        return True