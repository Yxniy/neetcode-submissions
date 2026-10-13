class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        maxi = 0
        if len(s) > 1:
            while right < len(s):
                
                if s[right] in s[left:right]:
                    left+=1
                else:
                    right+=1
                    maxi = max(maxi,right - left)

            return maxi
        else: return len(s)