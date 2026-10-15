class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = {}
        window = {}
        for i,s in enumerate(s1):
            freq[s] = freq.get(s,0) + 1
            window[s2[i]] = window.get(s2[i],0) + 1
            
            
            
        left = 0
        right = len(s1) - 1 
        
        while right < len(s2) -1:

            if freq == window:
                return True

            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left+=1
            right+=1

            window[s2[right]] = window.get(s2[right],0) + 1

        
        return freq==window






