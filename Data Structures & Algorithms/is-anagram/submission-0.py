class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for n in range(len(s)):
            map1[s[n:n+1]] = map1.get(s[n:n+1],0) +1
            map2[t[n:n+1]] = map2.get(t[n:n+1],0) +1
                

        return map1 == map2

        