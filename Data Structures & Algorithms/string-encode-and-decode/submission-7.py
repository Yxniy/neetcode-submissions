class Solution:

    def encode(self, strs: List[str]) -> str:
        
        for i in range(len(strs)):
            strs[i] = f"{len(strs[i])}#{strs[i]}"
        return "".join(strs)
    def decode(self, s: str) -> List[str]:
        
        if not s:
            return []
        result = []
        i = 0
        while(i <len(s)):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            result.append(s[j+1:j+length+1])
            i= length + 1 + j

        return result

        
        

