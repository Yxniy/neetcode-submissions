class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for n in range(len(s)):
            map1[s[n]] = map1.get(s[n],0) +1
            map2[t[n]] = map2.get(t[n],0) +1
                

        return map1 == map2

        