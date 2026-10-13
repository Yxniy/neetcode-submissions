class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}
        for string in strs:
            alpha = [0 for x in range(26)]
            
            for i in string:
                alpha[ord(i) - ord('a')] += 1
            
            if tuple(alpha) not in anagram:
                anagram[tuple(alpha)] = []

            anagram[tuple(alpha)].append(string)

        return list(anagram.values())
            


                