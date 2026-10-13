class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = {'{':'}', '(' : ')', '[':']'}
        if len(s) % 2 == 1:
            return False
        for n in s:
            if n in valid.keys():
                stack.append(n)
            elif n in valid.values():
                if len(stack) > 0 and valid[stack[-1]] == n:
                    stack.pop()
                else: return False
            else: return False
        
        return True if len(stack) == 0 else False